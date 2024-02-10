from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Product,Cart,Transaction
from django.shortcuts import redirect
import uuid, requests, json
from django.http import HttpResponse

# Create your views here.
def landingPage(request):
    return render(request, 'landingpage.html', {})

def signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        password = request.POST["password"]
        c_password = request.POST["c_password"]
        email = request.POST["email"]
        
        if password == c_password:
            if User.objects.filter(username=username).exists():
                print("Usernmae is already in use.")
                msg = "Username is already in use"
                return render(request, "signup.html",{'acc_created': msg})
            elif User.objects.filter(email=email).exists():
                print("Email is already in use.")
                msg = "Email is already in use"
                return render(request, "signup.html",{'acc_created': msg})
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=fname, last_name=lname)
                user.save()
                print('user created')
                return redirect('signin')
    return render (request, 'signup.html', {})

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('landingPage')
        else:
            print("Username or password is incorrect")
            msg = "Username or password is incorrect"
            return render(request, "signin.html", {'message': msg})
    return render(request, 'signin.html', {})

def shop(request):
    shop = Product.objects.all()
    return render(request, "shop.html", {'products' : shop,
                                         })

def product(request,pk):
    
    user_id = request.user.id
    request.session['product_id'] = pk
    
    prodct = Product.objects.get(id = pk)
    return render (request, "product.html", {
        'product': prodct,
        'user_id' : user_id,
    })
    
def cart(request):
    user_id = request.user.id
    carts = Cart.objects.filter(User_Details = user_id)
    subTotal = 0
    uuid_value = uuid.uuid4()
    
    # Calculate total price by iterating over each Cart object
    for cart in carts:
        subTotal += cart.Cart_Details.Product_Price * cart.Cart_Quantity
    return render(request, "cart.html", {'carts' : carts,
                                         'subTotal' : subTotal,
                                         'uuid' : uuid_value,
                                         })

def addCart(request):
     if request.method == "POST":
        quantity = int(request.POST["quantity"])
        product_id = request.session.get('product_id')  # Retrieve product ID from session
        user_id = request.user.id

        if product_id:
            product = Product.objects.get(id=product_id)
        
            # Check if the product is already in the cart for the current user
            existing_cart_items = Cart.objects.filter(Cart_Details=product_id, User_Details=user_id)

            if existing_cart_items.exists():
                # If the product is already in the cart, update the quantity
                cart_item = existing_cart_items.first()
                cart_item.Cart_Quantity += quantity  # Increment quantity
                cart_item.save()
            else:
                # If the product is not in the cart, create a new cart item
                cart = Cart(Cart_Quantity=quantity, Cart_Details=product, User_Details=User.objects.get(id=user_id))
                cart.save()
        
        # Clear the session variable after processing
        request.session.pop('product_id', None)
        
        return redirect('cart')

def removeCart(request,pk):
    user_id = request.user.id
    
    product_id = pk
    # Assuming each user can have only one cart
    cart = Cart.objects.filter(User_Details=user_id, Cart_Details=product_id).first()
    if cart:
        cart.delete()  # Delete the cart item from the database
    return redirect('cart')

def checkout(request):
    if request.method == "POST":
        subTotal = request.POST["subTotal"]
        uuid = request.POST["uuid"]
        return_url = request.POST["return_url"]
        
        sipping_inc = float(subTotal) + 10
        
        print("sipping inc",sipping_inc)
        
        subPaisa = (float(sipping_inc)) * 100
        
        user = request.user
        
        print(subPaisa)
        
        print("uuid",uuid)
        print("subTotal",subPaisa)
        print("return_url",return_url)
        print("user",user.username)
        
    url = "https://a.khalti.com/api/v2/epayment/initiate/"

    payload = json.dumps({
        "return_url": "http://127.0.0.1:8000" + return_url,
        "website_url": "http://127.0.0.1:8000",
        "amount": subPaisa,
        "purchase_order_id": uuid,
        "purchase_order_name": "test",
        "customer_info": {
        "name": user.username,
        "email": user.email,
        "phone": "9800000001"
        }
    })
    headers = {
        'Authorization': 'key a224c46665374ec098a119e8ee5939e9',
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    
    new_res = json.loads(response.text)
    print(new_res)
    
    # Save the transaction code in the db to validate transaction
    transaction_id = new_res['pidx']
    
    transaction = Transaction(Transaction_ID=transaction_id, Transaction_Amount=subPaisa, User_Details=User.objects.get(id=user.id))
    transaction.save()
        
    return redirect(new_res['payment_url'])

def success(request):
    pidx = request.GET['pidx']
    
    url = "https://a.khalti.com/api/v2/epayment/lookup/"
    
    headers = {
        'Authorization': 'key a224c46665374ec098a119e8ee5939e9',
        'Content-Type': 'application/json',
    }
    
    payload = json.dumps({
        "pidx": pidx
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    
    new_res = json.loads(response.text)
    print(new_res)
    
    #check for valid transaction form database and update the status
    #check for valid transaction by checking transaction id and userid
    if request.method == "POST":
        transaction = Transaction.objects.get(Transaction_ID=pidx)
        if transaction and transaction.User_Details.username == request.user.username:
            transaction.Transaction_Status = True
            transaction.save()
            return render(request, "success.html", {'pidx':pidx,
                                                    })
        else:
            print("Not a valid payment.")
            return HttpResponse("Unauthorized access or transaction not found.", status=401)
    else:
        return HttpResponse("Invalid request method.", status=405)

    

def logOut(request):
    logout(request)
    return redirect('landingPage')
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Product


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
    prodct = Product.objects.get(id = pk)
    return render (request, "product.html", {
        'product': prodct,
    })

def logOut(request):
    logout(request)
    return redirect('landingPage')
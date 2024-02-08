var check = false;

function changeVal(el) {
  var qt = parseFloat(el.parent().children(".qt").html());
  var price = parseFloat(el.parent().children(".price").html());
  var eq = Math.round(price * qt * 100) / 100;
  
  el.parent().children(".full-price").html( eq + "€" );
  
  changeTotal();			
}

// function changeTotal() {
  
//   var price = 0;
  
//   $(".full-price").each(function(index){
//     price += parseFloat($(".full-price").eq(index).html());
//   });
  
//   price = Math.round(price * 100) / 100;
//   // var tax = Math.round(price * 0.05 * 100) / 100
//   var shipping = parseFloat($(".shipping span").html());
//   var fullPrice = Math.round((price + shipping) *100) / 100;
  
//   if(price == 0) {
//     fullPrice = 0;
//   }
  
//   $(".subtotal span").html(price);
//   // $(".tax span").html(tax);
//   $(".total span").html(fullPrice);
// }


function changeTotal() {
  var totalPrice = 0;

  $(".product").each(function(index, product){
      var price = parseFloat($(product).find(".price").html());
      var quantity = parseInt($(product).find(".qt").html());
      var productTotalPrice = price * quantity;
      totalPrice += productTotalPrice;
      $(product).find(".full-price").html(productTotalPrice.toFixed(2));
  });

  var shipping = 10; // Assuming shipping cost is fixed at Rs. 10
  var fullPrice = totalPrice + shipping;

  $(".subtotal span").html(totalPrice.toFixed(2));
  $(".total span").html(fullPrice.toFixed(2));
}


$(document).ready(function(){
  
  $(".remove").click(function(){
    var el = $(this);
    el.parent().parent().addClass("removed");
    window.setTimeout(
      function(){
        el.parent().parent().slideUp('fast', function() { 
          el.parent().parent().remove(); 
          if($(".product").length == 0) {
            if(check) {
              $("#cart").html("<h1>The shop does not function, yet!</h1><p>If you liked my shopping cart, please take a second and heart this Pen on <a href='https://codepen.io/ziga-miklic/pen/xhpob'>CodePen</a>. Thank you!</p>");
            } else {
              $("#cart").html("<h1>No products!</h1>");
            }
          }
          changeTotal(); 
        });
      }, 200);
  });
  
  $(".qt-plus").click(function(){
    var currentQuantity = parseInt($(this).parent().children(".qt").html());
    
    // Check if the current quantity is less than 20 before incrementing
    if (currentQuantity < 20) {
        $(this).parent().children(".qt").html(currentQuantity + 1);

        $(this).parent().children(".full-price").addClass("added");

        var el = $(this);
        window.setTimeout(function(){el.parent().children(".full-price").removeClass("added"); changeVal(el);}, 150);
    } else {
        // If quantity is already 20, display a message or perform another action
        alert("You can only add up to 20 items.");
    }
});
  
  $(".qt-minus").click(function(){
    
    child = $(this).parent().children(".qt");
    
    if(parseInt(child.html()) > 1) {
      child.html(parseInt(child.html()) - 1);
    }
    
    $(this).parent().children(".full-price").addClass("minused");
    
    var el = $(this);
    window.setTimeout(function(){el.parent().children(".full-price").removeClass("minused"); changeVal(el);}, 150);
  });
  
  window.setTimeout(function(){$(".is-open").removeClass("is-open")}, 1200);
  
  $(".bth-checkout").click(function(){
    check = true;
    $(".remove").click();
  });
});
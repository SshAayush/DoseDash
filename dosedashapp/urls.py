from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.landingPage, name="landingPage"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logOut, name="logout"),
    path('shop/', views.shop, name="shop"),
    path('product/<str:pk>/', views.product, name="product"),
    path('cart/', views.cart, name="cart"),
    path('addCart', views.addCart, name="addCart"),
]

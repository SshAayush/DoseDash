from django.urls import include, path
from . import views


urlpatterns = [
    # path('', include('dosedashapp.urls')),
    path('', views.landingPage, name="landingPage"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logOut, name="logout"),
    path('shop/', views.shop, name="shop"),
    path('product/<str:pk>/', views.product, name="product"),
    path('cart/', views.cart, name="cart"),
    path('addCart', views.addCart, name="addCart"),
    path('removeCart/<str:pk>/', views.removeCart, name="removeCart"),
    path('checkout/', views.checkout, name="checkout"),
    path('success/', views.success, name="success"),
    path('addreminder/<str:pk>/', views.addreminder, name="addreminder"),
    path('contactus/', views.contactUs, name="contactus"),
    path('sendReminder/', views.sendReminder, name="sendReminder"),
    path('changePassword/', views.changePassword, name="changePassword"),
    path('search/', views.search, name="search"),
    path('profile/', views.profile, name="profile"),
    path('transactionHistory/', views.transactionHistory, name="transactionHistory"),
    path('updateprofile/', views.updateprofile, name="updateprofile"),
    path('viewreminder/', views.viewReminder, name="viewreminder"),
    path('deletereminder/<str:pk>', views.deleteReminder, name="deletereminder"),
    path('t/', views.test, name="test"),
]

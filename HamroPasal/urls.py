
from os import name
from django.urls import path
from . views import *

app_name='HamroPasal'
urlpatterns= [
   path("",HomeView.as_view(),name="home"),
   path('about/',AboutView.as_view(),name="about"),
   path('contact-us/',ContactView.as_view(),name="contact"),
   path('allproducts/',AllProductView.as_view(),name='allproducts'),
   path('product/<slug:slug>',ProductDetailView.as_view(),name='productdetail'),
   path('add-to-cart-<int:pro_id>/',AddToCartView.as_view(),name='addtocart'),
   path('my-cart/',MyCartView.as_view(),name='mycart'),
   path('manage-cart/<int:cp_id>/',ManageCartView.as_view(),name='managecart'),
   path('empty-cart/',EmptyCartView.as_view(),name='emptycart'),
   path('checkout/',CheckoutView.as_view(),name='checkout'),
   path("khalti-request/",KhaltiRequestView.as_view(),name='khaltirequest'),
   path("khalti-verify/",KhaltiVerifyView.as_view(),name='khaltiverify'),
   path("esewa-request/",EsewaRequestView.as_view(),name='esewarequest'),
   path("esewa-verify/",EsewaVerifyView.as_view(),name='esewaverify'),
   path('register/',CustomerRegistrationView.as_view(),name='customerregistration'),
   path('logout/',CustomerLogoutView.as_view(),name='customerlogout'),
   path('login/',CustomerLoginView.as_view(),name='customerlogin'),
   path('profile/',CustomerProfileView.as_view(),name='customerprofile'),
   path('profile/order-<int:pk>/',CustomerOrderDetailView.as_view(),name='customerorderdetail'),
   path('forgot-password/',PasswordForgotView.as_view(),name='passwordforgot'),
   path('password-reset/<email>/<token>/',PasswordResetView.as_view(),name='passwordreset'),
   path('admin-login/',AdminLoginView.as_view(),name='adminlogin'),
   path('admin-home/',AdminHomeView.as_view(),name='adminhome'),
   path('admin-order/<int:pk>/',AdminOrderDetailView.as_view(),name='adminorderdetail'),
   path('admin-all-orders/',AdminOrderListView.as_view(),name='adminorderlist'),
   path('admin-order-<int:pk>-change/',AdminOrderStatusChangeView.as_view(),name='adminorderstatuschange'),
   path('search/',SearchView.as_view(),name='search'),
]

from django.urls import path
from . views import *
from ecomapp import views


app_name = "ecomapp"

urlpatterns = [

    path("", HomeView.as_view(), name="home"),
    
    path("about/", AboutView.as_view(), name="about"),
    path("contact-us/", ContactView.as_view(), name="contact"),
    path("all-products/", AllProductsView.as_view(), name="allproducts"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="productdetail"),

    path('all-product-list/<int:cat_id>',
         views.All_product_list, name='all_product_list'),

    path('contact', views.contact, name='contact'),


    path('add-to-cart-<int:pro_id>', AddToCartView.as_view(), name='addtocart'),
    path('my-cart/', MyCartView.as_view(), name='mycart'),
    path('manage-cart/<int:cp_id>/', ManageCartView.as_view(), name='managecart'),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("register/", CustomerRegistrationView.as_view(), name="registercustomer"),
    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),
    path("profile/", CustomerProfileView.as_view(), name="customerprofile"),
    path("profile/order-<int:pk>", CustomerOrderDetailView.as_view(),
         name="customerorderdetail"),


    path('brand-product-list/<int:brand_id>',
         views.brand_product_list, name='brand-product-list'),


    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),
    path("admin-home/", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(),
         name="adminorderdetail"),
    path("admin-all-orders/", AdminOrderListView.as_view(), name="adminorderlist"),
    path("admin-order-<int:pk>-change/",
         AdminOrderStatusChangeView.as_view(), name="adminorderstatuschange"),
    path("admin-product/list/", AdminProductListView.as_view(),
         name="adminproductlist"),
    path("admin-product/add/", AdminProductCreateView.as_view(),
         name="adminproductcreate"),



    path("search/", SearchView.as_view(), name="search"),

    path("khalti-request/", KhaltiRequestView.as_view(), name="khaltirequest"),
    path("khalti-verify/", KhaltiVerifyView.as_view(), name="khaltiverify"),


    path("esewa-request/", EsewaRequestView.as_view(), name="esewarequest"),
    path("esewa-verify/", EsewaVerifyView.as_view(), name="esewaverify"),

    path("forgot-password/", PasswordForgotView.as_view(), name="passworforgot"),
    path("password-reset/<email>/<token>/",
         PasswordResetView.as_view(), name="passwordreset"),





]

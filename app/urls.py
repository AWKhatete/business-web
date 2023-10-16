from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import *

urlpatterns = [
    path("", views.home),
    path("contact/", views.contact, name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("productdetail/<int:pk>", views.ProductDetail.as_view(), name="productdetail"),
    path("categorytitle/<val>", views.CategoryTitle.as_view(), name="categorytitle"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("address/", views.address, name="address"),
    path("updateAddress/<int:pk>", views.updateAddress.as_view(), name="updateAddress"),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('checkout/', views.checkout.as_view(), name='checkout'),
     path('orders/', views.orders, name='orders'),

    path("pluscart/", views.plus_cart),
    path("minuscart/", views.minus_cart),
    path("removecart/", views.remove_cart),

    #anthentication urls
    path("registration/", views.CustomerRegistrationView.as_view(), name="registration"),
    path("accounts/login/", auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('passwordreset/', auth_view.PasswordResetView.as_view(template_name='app/passwordreset.html', form_class=PasswordResetForm), name='passwordreset'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=PasswordResetForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), 
    name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    #mpesa urls
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),

    # register, confirmation, validation and callback urls
    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),
    path('c2b/callback', views.call_back, name="call_back"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
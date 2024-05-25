
from django.contrib import admin
from. import views
from django.conf import settings
from django.urls import path,include
from . import views 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm




urlpatterns = [
    path("",views.home, name="home"),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkOut, name="checkout"),
    path("search/", views.searchProduct, name="search"),
    path("category/", views.categoryProduct, name="category"),
    path("details/", views.detailsProduct, name="details"),
    path("update_item/", views.updateItem, name="update_item"),
    path("contact/", views.contact, name="contact"),
    path("address/", views.address, name="address"),
    path("updateAddress/<int:pk>", views.UpdateAddress.as_view(),name="updateAddress"),
    
    
    #login
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path("logout/", views.my_logout_view, name='logout'), 
    
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),    name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header ="Gake"
admin.site.site_title="Gake"
admin.site.site_index_title ="Welcome to Gake Shop"
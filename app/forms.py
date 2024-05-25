from django import forms
import re
from django.contrib.auth.models import User
from .models import Comment, ShippingAddress
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm,UsernameField,SetPasswordForm,PasswordResetForm
from .models import Customer
# from .models import Customer





# hàm đăng ký người dùng 
class CustomerRegistrationForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password1= forms.CharField(label='Nhập mật khẩu',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='Nhập lại mật khẩu',widget=forms.PasswordInput(attrs={'class':'form-control'}))


    # def clean_password2(self):
    #     if 'password1' in self.cleaned_data:
    #         password1 = self.cleaned_data['password1']
    #         password2 = self.cleaned_data['password2']
    #         if password1 == password2 and password1:
    #             return password2
    #     raise forms.ValidationError("Mật khẩu không hợp lệ")

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if not re.search(r'^\w+$', username):
    #         raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
    #     try:
    #         User.objects.get(username=username)
    #     except User.DoesNotExist:
    #         return username
    #     raise forms.ValidationError("Tài khoản đã tồn tại")
   
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    #         raise forms.ValidationError("Địa chỉ email không hợp lệ")
    #     # try:
    #     # #   User.objects.get(email = email)
    #     #     User.objects.filter(email=email).first()
    #     #     test =  User.objects.filter(email=email).first()
    #     #     print("test",test)
    #     # except:
    #     #     return email
    #     # raise forms.ValidationError("Email đã tồn tại")
    
    #     user_by_email = User.objects.filter(email=email).first()
    #     if user_by_email is None:
    #         return email
    #     else:
    #         raise forms.ValidationError("Email đã tồn tại")

    # def save(self):
    #     User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'],first_name=self.cleaned_data['first_name'],last_name=self.cleaned_data['last_name'],)



class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.product = kwargs.pop('product', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.product = self.product.first()
        comment.save()

    class Meta:
        model = Comment
        fields = ["body"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

        
class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ("customer", "order", "address", "mobile")
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class  CustomerRegistrationForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1= forms.CharField(label='Passowrd',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='Confirm Passowrd',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
class Meta :
    model= User 
    fields = ['username','email' ,'password1','password2']
    
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs=
    {'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs=
    {'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs=
    {'autocomplete':'current-password','class':'form-control'}))
    
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs=
    {'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs=
    {'autocomplete':'current-password','class':'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'mobile', 'state', 'zipcode']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality': forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class': 'form-control'}), 
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class':'form-control'}),
        }

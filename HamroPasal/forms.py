from django import forms
from django.db.models.fields import EmailField
from django.forms.widgets import EmailInput, Widget
from .models import Customer, Order
from django.contrib.auth.models import User

class CheckOutForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['ordered_by','shipping_address','mobile','email','payment_method']

class CustomerRegistrationForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())
    email=forms.CharField(widget=forms.EmailInput())

    class Meta:
        model=Customer
        fields=["username","password","email","full_name","address"]

    def clean_username(self):
        uname=self.cleaned_data.get('username')
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("Customer with this username already exists")
        return uname


class CustomerLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())

class PasswordForgotForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={
    'class':'form-control',
    'placeholder':"Enter the email used in customer account"}))

    def clean_email(self):
        e=self.cleaned_data.get('email')
        if Customer.objects.filter(user__email=e).exists():
            pass
        else:
            raise forms.ValidationError("Customer with this account doesnt exists....")

        return e

class PasswordResetForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'autocomplete': 'new-password',
        'placeholder': 'Enter New Password',
    }), label="New Password")
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'autocomplete': 'new-password',
        'placeholder': 'Confirm New Password',
    }), label="Confirm New Password")

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        confirm_new_password = self.cleaned_data.get("confirm_new_password")
        if new_password != confirm_new_password:
            raise forms.ValidationError(
                "New Passwords did not match!")
        return confirm_new_password


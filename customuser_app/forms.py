from django import forms
from customuser_app.models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=60)
    displayname = forms.CharField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)

# from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm, forms
# from django.contrib.auth.models import User
# from post.models import Contact
# from django.urls import reverse_lazy
#
# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name', 'email', 'message']
#
# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'username', 'email', 'password1', 'password2']
#
# # class LoginForm(forms.Form):
# #     template_name = 'auth/login.html'
# #     form_class = LoginForm
# #     succes_url = reverse_lazy('/')
# #
# #     def form_valid(self, form):
# #         username

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from post.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

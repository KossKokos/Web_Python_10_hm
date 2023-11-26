from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, TextInput, PasswordInput, EmailField, EmailInput


class RegisterForm(UserCreationForm):
    username = CharField(max_length=100, widget=TextInput())
    email = EmailField(widget=EmailInput())
    password1 = CharField(max_length=20, min_length=8, widget=PasswordInput())
    password2 = CharField(max_length=20, min_length=8, widget=PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    # username = CharField(max_length=100, required=True, widget=TextInput())
    email = EmailField(widget=EmailInput())
    password = CharField(max_length=20, min_length=8, required=True, widget=PasswordInput())

    class Meta:
        model = User
        fields = ("email", "password")
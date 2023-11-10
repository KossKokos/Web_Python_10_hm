from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
# Create your views here.

def signupuser(request):
    if request.user.is_authenticated:
         redirect(to='quotes:root')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='users:login')
        else:
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})

def signinuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotes:root')
    
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, "User's name or password didn't match")
            return redirect(to='users:login')
        login(request, user)
        return redirect(to='quotes:root')
    return render(request, 'users/signin.html', context={'form': LoginForm()})

@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='quotes:root')
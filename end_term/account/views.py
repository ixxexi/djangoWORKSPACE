from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.shortcuts import redirect
# Create your views here.

def Login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in.')  # Success message
            return redirect('index')
        else:
            messages.error(request, 'Login failed. Please try again.')  # Error message for invalid form
    else:
        form = LoginForm()
    return render(request, 'account/login.html', locals())

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'You have successfully registered.')
            return redirect('index')  # Assuming 'index' is the name of your homepage URL pattern
        else:
            messages.error(request, 'Registration failed. Please try again.')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', locals())

def Account(request):
    return render(request, 'account/account.html')
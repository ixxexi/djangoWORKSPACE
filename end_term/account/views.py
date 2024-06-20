from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from mainsite.models import Auctions
from django.views.decorators.http import require_POST


def Login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('index')
        else:
            messages.error(request, 'Login failed. Please try again.')
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
            return redirect('index')
        else:
            messages.error(request, 'Registration failed. Please try again.')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', locals())

@login_required
def Account(request):
    user_auctions = Auctions.objects.filter(user=request.user).order_by('-end_time')
    context = {
        'auctions': user_auctions,
    }
    return render(request, 'account/account.html', context)

@require_POST
@login_required
def delete_auction(request, auction_id):
    auction = get_object_or_404(Auctions, auction_id=auction_id, user=request.user)
    auction.delete()
    return redirect('account')
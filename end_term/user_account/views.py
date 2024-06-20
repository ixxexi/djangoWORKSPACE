from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from mainsite.models import Auctions
from django.views.decorators.http import require_POST


def Login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if not request.POST.get("remember", None):
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(30 * 24 * 60 * 60)  # 30 days in seconds

            messages.success(request, "成功登入！")
            return redirect("index")
        else:
            messages.warning(request, "登入失敗，請再試一次。")
    else:
        form = LoginForm()
    return render(request, "user_account/login.html", locals())


def custom_logout(request):
    logout(request)
    messages.success(request, "您已成功登出。")
    return redirect("index")


def Register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "成功註冊！")
            return redirect("index")
        else:
            messages.warning(request, "註冊失敗，請再試一次。")
    else:
        form = RegisterForm()
    return render(request, "user_account/register.html", locals())


@login_required
def Account(request):
    user_auctions = Auctions.objects.filter(user=request.user).order_by("-start_time")
    context = {
        "auctions": user_auctions,
    }
    return render(request, "user_account/account.html", context)


@require_POST
@login_required
def delete_auction(request, auction_id):
    auction = get_object_or_404(Auctions, auction_id=auction_id, user=request.user)
    auction.delete()
    messages.success(request, "成功刪除拍賣品！")
    return redirect("account")

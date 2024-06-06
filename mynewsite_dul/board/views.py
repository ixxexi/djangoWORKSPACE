from django.shortcuts import render
from django.http import HttpResponseRedirect
from board import models
from . import forms
from django.contrib.sessions.models import Session
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
def index(request, pid=None, del_pass=None):
    # request.session.set_test_cookie()
    # if request.session.test_cookie_worked():
    #     request.session.delete_test_cookie()
    #     message = "Cookies 測試成功"
    # else:
    #     message = "Cookies 無法使用"
    # request.session.set_test_cookie()
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
        try:
            user = auth.models.User.objects.get(username=username)
            diaries = models.Diary.objects.filter(user=user).order_by("-created_at")
        except:
            pass
    return render(request, "board/index.html", locals())


def login(request):
    if request.method == "POST":
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST["username"].strip()
            password = request.POST["password"].strip()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, "成功登入")
                    return HttpResponseRedirect("/board/")
                else:
                    messages.add_message(request, messages.WARNING, "帳號未啟用")
            else:
                messages.add_message(request, messages.WARNING, "登入失敗")
        else:
            messages.add_message(request, messages.INFO, "請檢查輸入的欄位")
    else:
        login_form = forms.LoginForm()
    return render(request, "board/login.html", locals())


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, "成功登出")
    return HttpResponseRedirect("/board/")


@login_required(login_url="/board/login/")
def posting(request):
    # years = range(1960, 2021)
    # posts = models.Post.objects.filter(enabled=True).order_by("-pub_time")[:30]
    # moods = models.Mood.objects.all()
    post_form = forms.PostForm()
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)

    if request.method == "POST":
        user = auth.models.User.objects.get(username=username)
        diary = models.Diary(user=user)
        post_form = forms.DiaryForm(request.POST, instance=diary)
        if post_form.is_valid():
            messages.add_message(request, messages.INFO, "日記已儲存")
            post_form.save()
            return HttpResponseRedirect("/board/")
        else:
            messages.add_message(request, messages.WARNING, "請檢查輸入的欄位")
    else:
        post_form = forms.DiaryForm()
        messages.add_message(request, messages.WARNING, "請檢查輸入的欄位")
    return render(request, "board/posting.html", locals())
    # try:
    #     user_id = request.POST["user_id"]
    #     user_pass = request.POST["user_pass"]
    #     user_post = request.POST["user_post"]
    #     user_mood = request.POST["mood"]
    #     user_byear = request.POST["byear"]
    # except:
    #     user_id = None
    #     message = "未填寫完整"

    # if user_id != None:
    #     mood = models.Mood.objects.get(status=user_mood)
    #     post = models.Post.objects.create(
    #         mood=mood,
    #         nickname=user_id,
    #         message=user_post,
    #         del_pass=user_pass,
    #         byear=user_byear,
    #     )
    #     post.save()
    #     message = "成功儲存"


def listing(request):
    posts = models.Post.objects.filter(enabled=True).order_by("-pub_time")[:30]
    moods = models.Mood.objects.all()
    return render(request, "board/listing.html", locals())


def contact(request):
    contact_form = forms.ContactForm()
    if request.method == "POST":
        contact_form = forms.ContactForm(request.POST)
        if contact_form.is_valid():
            user_name = contact_form.cleaned_data["user_name"]
            user_city = contact_form.cleaned_data["user_city"]
            user_school = contact_form.cleaned_data["user_school"]
            user_email = contact_form.cleaned_data["user_email"]
            user_message = contact_form.cleaned_data["user_message"]
            message = "感謝您的來信"
            contact_form.save()
        else:
            message = "請檢查您輸入的資訊是否正確"
    else:
        form = forms.ContactForm()
    return render(request, "board/contact.html", locals())


@login_required(login_url="/board/login/")
def profile(request):
    if request.user.is_authenticated:
        username = request.user.username
    user = auth.models.User.objects.get(username=username)
    try:
        profile = models.Profile.objects.get(user=user)
    except:
        profile = Profile(user)

    if request.method == "POST":
        profile_form = forms.ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(request, messages.INFO, "個人資料已儲存")
            return HttpResponseRedirect("/board/profile/")
        else:
            messages.add_message(request, messages.WARNING, "請檢查輸入的欄位")
    else:
        profile_form = forms.ProfileForm()
    return render(request, "board/profile.html", locals())

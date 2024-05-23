from django.shortcuts import render
from django.http import HttpResponseRedirect
from board import models
from . import forms


# Create your views here.
def index(request, pid=None, del_pass=None):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        message = "Cookies 測試成功"
    else:
        message = "Cookies 無法使用"
    request.session.set_test_cookie()
    return render(request, "board/index.html", locals())


def posting(request):
    years = range(1960, 2021)
    posts = models.Post.objects.filter(enabled=True).order_by("-pub_time")[:30]
    moods = models.Mood.objects.all()
    post_form = forms.PostForm()
    if request.method == "POST":
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            message = "成功儲存"
            post_form.save()
            return HttpResponseRedirect("/board/list/")
        else:
            message = "資料有誤"
    else:
        post_form = forms.PostForm()
        message = "請輸入資料"
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

from django.shortcuts import render
from board import models


# Create your views here.
def index(request, pid=None, del_pass=None):
    # try:
    #     uid = request.GET["user_id"]
    #     upass = request.GET["user_pass"]
    #     byear = request.GET["byear"]
    #     fcolor = request.GET.getlist["fcolor"]
    # except:
    #     uid = None
    #     upass = None
    # if uid != None and upass == "12345":
    #     verified = True
    # else:
    #     verified = False

    years = range(1960, 2021)
    posts = models.Post.objects.filter(enabled=True).order_by("-pub_time")[:30]
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET["user_id"]
        user_pass = request.GET["user_pass"]
        user_post = request.GET["user_post"]
        user_mood = request.GET["mood"]
        user_byear = request.GET["byear"]
    except:
        user_id = None
        message = "未填寫完整"

    if pid and del_pass:
        try:
            post = models.Post.objects.get(id=pid)
        except:
            post = None
        if post.del_pass == del_pass:
            post.delete()
            message = "留言已刪除"
        else:
            message = "密碼錯誤"

    elif user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(
            mood=mood,
            nickname=user_id,
            message=user_post,
            del_pass=user_pass,
            byear=user_byear,
        )
        post.save()
        message = "成功儲存"
    return render(request, "board/index.html", locals())


def posting(request):
    moods = models.Mood.objects.all()
    try:
        user_id = request.post["user_id"]
        user_pass = request.post["user_pass"]
        user_post = request.post["user_post"]
        user_mood = request.post["mood"]
        user_byear = request.post["byear"]
    except:
        user_id = None
        message = "未填寫完整"

    if user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(
            mood=mood,
            nickname=user_id,
            message=user_post,
            del_pass=user_pass,
            byear=user_byear,
        )
        post.save()
        message = "成功儲存"
    return render(request, "board/posting.html", locals())

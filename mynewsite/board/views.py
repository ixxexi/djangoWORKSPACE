from django.shortcuts import render
from board import models


# Create your views here.
def index(request):
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
    return render(request, "board/index.html", locals())

from django.db import models
from django.contrib import auth


# Create your models here.
class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.status


class Diary(models.Model):
    user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
    budget = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    note = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return "{}({})".format(self.user.username, self.created_at)


class Profile(models.Model):
    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    height = models.IntegerField(default=170)
    male = models.BooleanField(default=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    mood = models.ForeignKey("Mood", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, default="anonymous")
    message = models.TextField(null=False)
    byear = models.IntegerField(default=1980)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.message


class Contact(models.Model):
    CITY = [
        ["TP", "Taipei"],
        ["TY", "Taoyuan"],
        ["TC", "Taichung"],
        ["TN", "Tainan"],
        ["KS", "Kaohsiung"],
        ["NA", "Others"],
    ]
    user_name = models.CharField(max_length=10)
    user_city = models.CharField(max_length=10, choices=CITY, default="TP")
    user_school = models.BooleanField(default=False)
    user_email = models.EmailField()
    user_message = models.TextField(null=False)

    def __str__(self):
        return self.user_message


class User(models.Model):
    username = models.CharField(max_length=10, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.username

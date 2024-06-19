from django import forms
from . import models
from captcha.fields import CaptchaField


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = models.Contact
#         fields = ["user_name", "user_city", "user_school", "user_email", "user_message"]

#     def __init__(self, *args, **kwargs):
#         super(ContactForm, self).__init__(*args, **kwargs)
#         self.fields["user_name"].label = "姓名"
#         self.fields["user_city"].label = "居住城市"
#         self.fields["user_school"].label = "是否在學"
#         self.fields["user_email"].label = "電子郵件"
#         self.fields["user_message"].label = "意見"


# class DateInput(forms.DateInput):
#     input_type = "date"


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = models.Profile
#         fields = ["height", "male", "website"]

#     def __init__(self, *args, **kwargs):
#         super(ProfileForm, self).__init__(*args, **kwargs)
#         self.fields["height"].label = "身高(cm)"
#         self.fields["male"].label = "是男生嗎?"
#         self.fields["website"].label = "個人網站"


# class DiaryForm(forms.ModelForm):
#     class Meta:
#         model = models.Diary
#         fields = ["budget", "weight", "note", "created_at"]
#         widgets = {"created_at": DateInput()}

#     def __init__(self, *args, **kwargs):
#         super(DiaryForm, self).__init__(*args, **kwargs)
#         self.fields["budget"].label = "今日花費"
#         self.fields["weight"].label = "今日體重"
#         self.fields["note"].label = "日記"
#         self.fields["created_at"].label = "日期"


# class PostForm(forms.ModelForm):
#     captcha = CaptchaField()

#     class Meta:
#         model = models.Post
#         fields = ["mood", "nickname", "message", "byear", "del_pass"]

#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields["mood"].label = "現在心情"
#         self.fields["nickname"].label = "暱稱"
#         self.fields["message"].label = "留言"
#         self.fields["byear"].label = "出生年"
#         self.fields["del_pass"].label = "密碼"
#         self.fields["captcha"].label = "驗證碼"


# class LoginForm(forms.Form):
#     username = forms.CharField(label="帳號", max_length=10)
#     password = forms.CharField(label="密碼", widget=forms.PasswordInput())
#     captcha = CaptchaField()
    # colors = (["紅", "紅"], ["綠", "綠"], ["藍", "藍"])
    # usercolor = forms.ChoiceField(label="喜歡的顏色", choices=colors)

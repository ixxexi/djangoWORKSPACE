from django import forms
from . import models
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ["user_name", "user_city", "user_school", "user_email", "user_message"]

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["user_name"].label = "姓名"
        self.fields["user_city"].label = "居住城市"
        self.fields["user_school"].label = "是否在學"
        self.fields["user_email"].label = "電子郵件"
        self.fields["user_message"].label = "意見"


class PostForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = models.Post
        fields = ["mood", "nickname", "message", "byear", "del_pass"]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["mood"].label = "現在心情"
        self.fields["nickname"].label = "暱稱"
        self.fields["message"].label = "留言"
        self.fields["byear"].label = "出生年"
        self.fields["del_pass"].label = "密碼"
        self.fields["captcha"].label = "驗證碼"

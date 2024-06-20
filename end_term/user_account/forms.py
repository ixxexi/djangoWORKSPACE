from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "帳號"}),
        label="帳號",
        help_text="請輸入您的帳號",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "密碼"}
        ),
        label="密碼",
        help_text="請輸入您的密碼",
    )
    captcha = CaptchaField(label="驗證碼", help_text="請輸入圖中的驗證碼")


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "帳號"}),
        label="帳號",
        help_text="選擇一個帳號",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "電子郵件"}
        ),
        label="電子郵件",
        help_text="請輸入您的電子郵件地址",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "密碼"}
        ),
        label="密碼",
        help_text="創建一個密碼",
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "確認密碼"}
        ),
        label="確認密碼",
        help_text="再次輸入您的密碼",
    )
    captcha = CaptchaField(label="驗證碼", help_text="請輸入圖中的驗證碼")

    class Meta:
        model = User
        fields = ("username", "email", "password", "confirm_password", "captcha")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error("confirm_password", "兩個密碼不一致")

        return cleaned_data

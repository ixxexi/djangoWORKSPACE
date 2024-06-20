from django import forms
from . import models
from captcha.fields import CaptchaField
from django.forms import ModelForm
from .models import Auctions

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auctions
        fields = ['title', 'description', 'duration', 'starting_bid']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
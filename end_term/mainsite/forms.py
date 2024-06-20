from django import forms
from .models import Auctions


class AuctionForm(forms.ModelForm):
    days = forms.IntegerField(
        min_value=0, required=False, initial=0, label="天", help_text="拍賣持續天數"
    )
    hours = forms.IntegerField(
        min_value=0,
        max_value=23,
        required=False,
        initial=0,
        label="小時",
        help_text="拍賣持續小時數",
    )
    minutes = forms.IntegerField(
        min_value=0,
        max_value=59,
        required=False,
        initial=0,
        label="分鐘",
        help_text="拍賣持續分鐘數",
    )

    class Meta:
        model = Auctions
        fields = [
            "title",
            "description",
            "starting_bid",
            "days",
            "hours",
            "minutes",
            "image",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "標題"}),
            "description": forms.Textarea(attrs={"rows": 3, "placeholder": "描述"}),
            "starting_bid": forms.NumberInput(
                attrs={"step": 1, "placeholder": "起始價"}
            ),
        }

    def save(self, commit=True):
        auction = super(AuctionForm, self).save(commit=False)
        days = self.cleaned_data.get("days", 0)
        hours = self.cleaned_data.get("hours", 0)
        minutes = self.cleaned_data.get("minutes", 0)
        auction.duration = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60)
        if commit:
            auction.save()
        return auction

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Auctions, Bids

admin.site.register(Auctions)
admin.site.register(Bids)

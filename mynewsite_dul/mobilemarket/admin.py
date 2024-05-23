from django.contrib import admin
from mobilemarket.models import Maker, PModel, Product, PPhoto


class ProductAdmin(admin.ModelAdmin):
    list_display = ("nickname", "pmodel", "year", "price")
    search_fields = ("nickname", "pmodel__name")
    list_filter = ("pmodel", "year")
    ordering = ("-price",)


# Register your models here.
admin.site.register(Maker)
admin.site.register(PModel)
admin.site.register(Product)
admin.site.register(PPhoto)

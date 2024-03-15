from django.contrib import admin
from .models import NewTable, Product #(admin和models同一層)

# Register your models here.
admin.site.register(NewTable)
admin.site.register(Product)
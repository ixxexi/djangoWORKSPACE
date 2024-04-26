from django.contrib import admin
from .models import NewTable, Product # .相對路徑(admin和models同一層)

# Register your models here.
admin.site.register(NewTable)
admin.site.register(Product)
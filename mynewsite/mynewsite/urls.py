"""mynewsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from mysite.views import about,listing, homepage, week4HW
from mysite import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', homepage),
    path('about/', about),
    path('about/<int:author_no>/', about, name='about-url'),
    path('list/', listing),
    #path('list/<str:sku>', disp_detail),
    path('list/<int:year>/<int:month>/<int:day>/', listing, name='list-url'),
    path('week4/<int:ID>/<str:name>/<int:age>/', week4HW, name='week4-url'),

]

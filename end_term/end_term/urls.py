"""
URL configuration for end_term project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from mainsite import views as mainsite_views
from user_account.views import custom_logout
from user_account import views as account_views
from django.urls import re_path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", account_views.Account, name="account"),
    path("", mainsite_views.index, name="index"),
    path("accounts/login/", account_views.Login, name="login"),
    path("accounts/register/", account_views.Register, name="register"),
    re_path(r"^captcha/", include("captcha.urls")),
    path(
        "auction/<int:auction_id>/",
        mainsite_views.auction_detail,
        name="auction_detail",
    ),
    path("logout/", custom_logout, name="logout"),
    path(
        "auction/delete/<int:auction_id>/",
        account_views.delete_auction,
        name="delete_auction",
    ),
    path("auction/new/", mainsite_views.create_auction, name="new_auction"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

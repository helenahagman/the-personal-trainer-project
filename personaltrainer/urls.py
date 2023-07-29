"""
personaltrainer URL Configuration

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ptproject.urls"), name="ptproject-urls"),
    path("accounts/", include("allauth.urls")),
]

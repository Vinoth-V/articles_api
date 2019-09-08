from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLogoutAPIView,
    UserLoginAPIView
    )

urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name='Login'),
    url(r'^logout/$', UserLogoutAPIView.as_view(), name='Logout'),
    url(r'^signup/$', UserCreateAPIView.as_view(), name='Signup'),
]

from django.conf.urls import url
from django.contrib import admin
from .views import home, register

from . import views

urlpatterns = [
    url(r'^$', home),
    url(r'^register/', register),
]
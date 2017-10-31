from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^register/', views.register),
    url(r'^cart/', views.view_cart),
    url(r'^orders/', views.view_orders),
]

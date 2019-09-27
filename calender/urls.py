from django.contrib import admin
from django.conf.urls import include,url
from calender import views

urlpatterns = [
    url(r'', views.index, name="calender"),
]
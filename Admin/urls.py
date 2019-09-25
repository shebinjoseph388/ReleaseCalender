from django.contrib import admin
from django.conf.urls import url,include
from Admin import views

urlpatterns = [
    url(r'createRelease/', views.createRelease, name="createRelease"),
    url(r'CreateRelease/', views.CreateRelease, name="CreateRelease"),
    url(r'editRelease/', views.editRelease, name="editRelease"),
    url(r'EditRelease/', views.EditRelease, name="EditRelease"),
]
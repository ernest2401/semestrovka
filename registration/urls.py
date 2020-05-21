from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.RegisterFormView.as_view(),name='register'),
]

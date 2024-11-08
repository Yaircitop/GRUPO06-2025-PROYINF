from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.crear_boletin, name='crear_boletin'),
]

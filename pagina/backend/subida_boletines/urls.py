from django.urls import path
from . import views

urlpatterns = [
    path('', views.subir_boletin, name= 'subir_boletin'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.signup_view, name='signup'),  # Página de signup
]

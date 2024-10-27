from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



def home_view(request):
    return render(request, 'index.html')  # O el nombre de tu archivo HTML principal




from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')  # O el nombre de tu archivo HTML principal

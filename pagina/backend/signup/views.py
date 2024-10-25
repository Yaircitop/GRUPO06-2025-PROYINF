from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError
from .models import UserProfile

def signup_view(request):
    if request.method == 'POST':
        run = request.POST['run']
        username = request.POST['email']
        password = request.POST['password']
        
        try:
            # Verifica si ya existe un usuario con el mismo RUN
            if UserProfile.objects.filter(run=run).exists():
                return render(request, 'index.html', {
                    'error': 'El RUN ya está registrado, por favor intenta con otro.'
                })

            # Crear el usuario utilizando el email como username
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # Crear el perfil del usuario y guardar el RUN
            user_profile = UserProfile(user=user, run=run)
            user_profile.save()

            # Autenticar y redirigir al login
            login(request, user)
            return redirect('login')
        
        except IntegrityError:
            return render(request, 'index.html', {
                'error': 'Ya existe un usuario con este correo electrónico.'
            })
    
    return render(request, 'index.html')


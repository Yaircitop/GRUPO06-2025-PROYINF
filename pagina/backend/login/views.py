from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('home')  # Redirige a la página principal después del login
        else:

            print(form.errors)  # Imprime los errores del formulario
            return render(request, 'index.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})

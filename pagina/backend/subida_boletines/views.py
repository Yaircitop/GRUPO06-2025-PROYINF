from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import boletines_form

def subir_boletin(request):
    if request.method == 'POST':
        form = boletines_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = boletines_form
    return render(request, 'subir_boletin.html', {'form': form})
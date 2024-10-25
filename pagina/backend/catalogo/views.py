from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Boletines

def lista_boletines(request):
    categoria = request.GET.get('categoria')
    categorias = Boletines.objects.values_list('categoria', flat=True).distinct()
    if categoria:
        pdfs = Boletines.objects.filter(categoria=categoria)
    else:
        pdfs = Boletines.objects.all()
    return render(request, 'catalogo.html', {
        'pdfs': pdfs,
        'categorias':categorias,
        'categoria_seleccionada': categoria,
    })

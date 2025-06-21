from django.shortcuts import render, redirect
from .forms import NewsForm, KeywordForm
from .models import News
from .utils import summarize_news
from django.db.models import Q
from django.http import HttpResponse
from docx import Document
from io import BytesIO 
import io

def crear_boletin(request):
    news_form = NewsForm()
    keyword_form = KeywordForm()
    summarized_news = []

    if request.method == "POST":
        # Revisamos qué botón fue presionado
        if "upload_news" in request.POST:
            # Procesar el formulario de "Subir Noticia"
            news_form = NewsForm(request.POST)
            if news_form.is_valid():
                # Guardar la noticia en la base de datos
                news_form.save()
                return redirect('crear_boletin')  # Redirige a la misma página después de guardar

        elif "search_and_summarize" in request.POST:
            # Procesar el formulario de "Crear Boletín y Resumir"
            keyword_form = KeywordForm(request.POST)
            if keyword_form.is_valid():
                # Obtener palabras clave ingresadas
                keywords = keyword_form.cleaned_data['keywords']
                keyword_list = [word.strip() for word in keywords.split(",")]

                # Construir la consulta para buscar noticias relevantes
                query = Q()
                for keyword in keyword_list:
                    query |= Q(title__icontains=keyword) | Q(content__icontains=keyword)

                # Filtrar las noticias que coincidan con las palabras clave
                relevant_news = News.objects.filter(query).distinct()  # Evita duplicados
                summarized_news = summarize_news(relevant_news)
                doc = Document()
                doc.add_heading("Boletín Informativo", level=1)
                doc.add_paragraph("")  # Espacio

                for item in summarized_news:
                    doc.add_heading(item['title'], level=2)
                    doc.add_paragraph(item['summary'])
                    doc.add_paragraph("")  # Espacio entre noticias

                # 🔹 Guardar el documento en memoria
                buffer = BytesIO()
                doc.save(buffer)
                buffer.seek(0)

                # 🔹 Respuesta HTTP para descarga
                response = HttpResponse(buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                response['Content-Disposition'] = 'attachment; filename="boletin_resumen.docx"'
                return response

    return render(request, 'crear_boletin.html', {
        'news_form': news_form,
        'keyword_form': keyword_form,
        'summarized_news': summarized_news,
    })

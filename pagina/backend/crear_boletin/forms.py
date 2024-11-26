from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'date']  # Deben coincidir con los campos del modelo
        labels = {  # Traducción de las etiquetas
            'title': 'Título',
            'content': 'Contenido',
            'date': 'Fecha',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título de la noticia',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escriba el contenido de la noticia',
                'rows': 5,
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }

class KeywordForm(forms.Form):
    keywords = forms.CharField(
        label='Palabras clave',
        help_text='Ingrese palabras clave separadas por comas',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ejemplo: economía, política, tecnología',
        })
    )

from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'date']

class KeywordForm(forms.Form):
    keywords = forms.CharField(
        label='Palabras clave',
        help_text='Ingrese palabras clave separadas por comas',
        widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: economía, política, tecnología'})
    )


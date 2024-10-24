from django import forms
from catalogo.models import Boletines

class boletines_form(forms.ModelForm):
    class Meta:
        model = Boletines
        fields = ['titulo', 'categoria', 'file']
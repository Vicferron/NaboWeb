from django import forms
from Naboform.models import Infonabo

class Formnabo(forms.ModelForm):
    class Meta:
        model=Infonabo
        fields=('usuario', 'precio', 'entrada', 'contacto', 'time',)


class FormularioContacto(forms.Form):
    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()       
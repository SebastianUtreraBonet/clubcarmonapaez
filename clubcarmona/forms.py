from django import forms
from datetime import timedelta
from .models import *
class FormularioContacto(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control'}))
    socio = forms.IntegerField(label="NºSocio", widget=forms.NumberInput(attrs={'class': 'form-control'}), max_value=99999,
                              min_value=0)
    dni = forms.CharField(label="DNI", widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=9, min_length=9)
    evento = forms.ModelChoiceField(queryset=Carrera.objects.all().order_by('fecha').reverse().filter(fecha__gt=timezone.datetime.today() + timedelta(days=1)),
                                  widget=forms.Select(attrs={'class': 'form-control'}), label="Carrera")
    comentario = forms.CharField(label="Comentario", widget=forms.Textarea(attrs={'class':'form-control','cols':30,'rows':5,'style':'resize:none;', 'placeholder':'sin comentarios', 'default':'9'}), max_length=99999)


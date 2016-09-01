from django import forms
from datetime import timedelta
from .models import *
class FormularioContacto(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Dirección Email'}))
    socio = forms.IntegerField(label="NºSocio", widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Nº de Socio'}), max_value=99999,
                              min_value=0)
    dni = forms.CharField(label="DNI", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'DNI'}), max_length=9, min_length=9)
    sel = Carrera.objects.order_by('fecha').filter(fecha__gt=timezone.datetime.today() + timedelta(days=1))
    evento = forms.ModelChoiceField(queryset=sel,empty_label='Selecciona un evento',
                                  widget=forms.Select(attrs={'class': 'form-control','placeholder':'empty_label'}), label="Carrera")
    comentario = forms.CharField(label="Comentario", widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Introduce comentario','cols':30,'rows':5,'style':'resize:none;'}), max_length=99999)


from django.shortcuts import render
from django.utils import timezone
from clubcarmona.models import *

def post_list(request):
	posts = Carrera.objects.all()
	return render(request, 'Club/post_list.html', {'posts': posts})


def calendario(request):
	hoy = timezone.datetime.today()
	carrera = Carrera.objects.all()
	rango = ["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]
	return render(request, 'Club/calendario.html', {
			'hoy'     : hoy,
			'carrera':carrera,
			'rango':rango,

	})

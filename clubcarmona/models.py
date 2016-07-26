from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
	autor = models.ForeignKey('auth.User')
	titulo = models.CharField(max_length=250)
	texto = RichTextField(max_length=99999999)
	fecha = models.DateTimeField(default=timezone.now)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)
	foto = models.ImageField(upload_to='static/img/proximosEventos', default="nofoto.jpg", null=True)

	def publicacion(self):
		self.fecha_publicacion = timezone.now
		self.save()

	def __str__(self):
		return self.titulo


class Tipo(models.Model):
	tipo = models.CharField(max_length=200)

	def __str__(self):
		return self.tipo

class Carrera(models.Model):
	titulo = models.CharField(max_length=250)
	fecha = models.DateTimeField(default=timezone.now)
	foto = models.ImageField(upload_to='static/img/proximosEventos', default="nofoto.jpg", null=True)
	texto = models.CharField(max_length=99999, blank=True, null=True)
	link = models.CharField(max_length=200, blank=True, null=True)
	ciudad = models.CharField(max_length=200, blank=True, null=True)
	provicia = models.CharField(max_length=200, default='Cádiz')
	distancia = models.IntegerField(blank=True, null=True)
	precio = models.ImageField(default=0, blank=True, null=True)
	tipo = models.ForeignKey(Tipo)

	def __str__(self):
		return self.titulo

class Albumes(models.Model):
	nombre = models.CharField(max_length=250)
	direccion = models.CharField(max_length=400)
	foto = models.ImageField(default='nofoto.jpg',upload_to='static/img/fotografos', null=True)

	def __str__(self):
		return self.nombre

class Resultados(models.Model):
	carrera = models.ForeignKey(Carrera)
	enlace = models.FileField(upload_to='static/resultados', null=True)

	def __str__(self):
		return self.carrera.titulo
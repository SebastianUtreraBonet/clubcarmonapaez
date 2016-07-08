from django.db import models
from django.utils import timezone


# Create your models here.


class Post(models.Model):
	autor = models.ForeignKey('auth.User')
	titulo = models.CharField(max_length=250)
	texto = models.TextField()
	fecha = models.DateTimeField(default=timezone.now)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)

	def publicacion(self):
		self.fecha_publicacion = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo

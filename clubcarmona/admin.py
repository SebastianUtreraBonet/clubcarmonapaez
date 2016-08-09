from django.contrib import admin

from .models import Post,Carrera,Albumes,Resultados,Tipo

# Register your models here.

admin.site.register(Post)
admin.site.register(Carrera)
admin.site.register(Albumes)
admin.site.register(Resultados)
admin.site.register(Tipo)


from django.contrib import admin

from .models import Post,Carrera,Albume,Tipo,Participante,Liga

# Register your models here.

admin.site.register(Post)
admin.site.register(Carrera)
admin.site.register(Albume)
admin.site.register(Liga)
admin.site.register(Tipo)
admin.site.register(Participante)


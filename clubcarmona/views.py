from django.core.paginator import Paginator
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils import timezone
from datetime import datetime, date, time, timedelta
from django.utils.safestring import mark_safe


from clubcarmona.models import *





def post_list1(request):
	post = Post.objects.all().order_by('fecha_publicacion')
	return render(request, 'Club/post_list.html', {'posts':post})

def calendario(request):
    hoy = timezone.datetime.today()
    carreras = Carrera.objects.all()
    mes = {1:"ENERO",2:"FEBRERO",3:"MARZO",4:"ABRIL",5:"MAYO",6:"JUNIO",7:"JULIO",8:"AGOSTO",9:"SEPTIEMBRE",int(10):"OCTUBRE",int(11):"NOVIEMBRE",int(12):"DICIEMBRE"}
    dias = timezone.datetime.today()+timedelta(days=20)
    return render(request, 'Club/calendario.html',{
            'hoy'     : hoy,
            'carreras':carreras,
            'mes':mes,
            'dias':dias
    })


def carrera(request):
	path = request.path[9::]
	carrera = Carrera.objects.filter(pk=path)
	hora = calcularHora(Carrera.objects.filter(pk=path))
	print(hora)
	return render(request, 'Club/carrera.html',{'carrera':carrera, 'hora':hora,})



def ficha(request):
	path = request.path[7::]
	posts = Post.objects.filter(pk=path)
	hora = calcularHora(Post.objects.filter(pk=path))
	print(hora)
	return render(request, 'Club/ficha.html',{'posts':posts, 'hora':hora})



def galeria(request):
    album = Albumes.objects.all()
    color = ['forestgreen','blueviolet','coral','deeppink','darkorange','darkgreen','crimson','deepskyblue']
    return render(request, 'Club/galeria.html',{'album':album,'color':color})



def calcularHora(posts):
	hora=00
	minu=00
	hor = ""
	for i in posts:
		hora = i.fecha.hour+2
		minu = i.fecha.minute
	hor = str(hora)+":"+str(minu)
	return hor


def resultados(request):
    resultado = Resultados.objects.all()
    carrera = Carrera.objects.all().order_by('fecha')
    hoy = timezone.datetime.today()
    return render(request, 'Club/resultados.html',{'resultado':resultado, 'carrera':carrera, 'hoy':hoy})

def Paginador(request, modelo, paginas, nonRegPag):

   #Retorna el objeto paginator para comenzar el trabajo
   result_list = Paginator(modelo, paginas)
   try:
     #Tomamos el valor de parametro page, usando GET
     page = int(request.GET.get('page'));
   except:
     page = 1

   #Si es menor o igual a 0 igualo en 1
   if page <= 0:
     page = 1

   #Si el parámetro es mayor a la cantidad
   #de paginas le igualo el parámetro con las cant de paginas
   if(page > result_list.num_pages):
      page = result_list.num_pages

   #Verificamos si esta dentro del rango
   if (result_list.num_pages >= page):
       #Obtengo el listado correspondiente al page
       pagina = result_list.page(page)
       Contexto = {nonRegPag: pagina.object_list, #Asignamos registros de la pagina
                   'page': page, #Pagina Actual
                   'pages': result_list.num_pages, #Cantidad de Paginas
                   'has_next': pagina.has_next(), #True si hay proxima pagina
                   'has_prev': pagina.has_previous(), #true si hay Pagina anterior
                   'next_page': page+1, #Proxima pagina
                   'prev_page': page-1, #Pagina Anterior
                   'firstPage': 1,
                   }
       return Contexto

def post_list(request):
   #Obtengo los post de mi blog
   hoy = timezone.datetime.today()
   carreras = Carrera.objects.all()[0:10:]
   resultado = Resultados.objects.all()[0:10:]
   carrera = Carrera.objects.all().order_by('fecha')
   mes = {1:"ENERO",2:"FEBRERO",3:"MARZO",4:"ABRIL",5:"MAYO",6:"JUNIO",7:"JULIO",8:"AGOSTO",9:"SEPTIEMBRE",int(10):"OCTUBRE",int(11):"NOVIEMBRE",int(12):"DICIEMBRE"}
   dias = timezone.datetime.today()+timedelta(days=20)
   init_post = Post.objects.all().order_by("titulo")
   #Inicio el paginador
   pag = Paginador(request, init_post, 10, 'posts')
   n = 250
   cxt = {'posts': pag['posts'],
            'totPost': init_post,
            'paginator': pag,
            'n':n,
            'hoy'     : hoy,
            'carreras':carreras,
            'mes':mes,
            'dias':dias,
            'resultado':resultado,
            'carrera':carrera,
          }
   return render(request, 'Club/post_list.html',cxt)



def imagenes(request):
    a = Albumes.objects.all()
    return (request,'Club/galeria.html',{'a':a} )
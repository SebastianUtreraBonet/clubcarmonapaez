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
    rango = ["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]
    dias10 = timezone.datetime.today()+timedelta(days=10)
    print(dias10,'hola')
    return render(request, 'Club/calendario.html', {
            'hoy'     : hoy,
            'carreras':carreras,
            'rango':rango,
            'dias10':dias10
    })

def meses(request):
    mes = request.path[12::].upper()
    return render(request,'Club/meses.html',{'mes':mes})

def ficha(request):
	path = request.path[7::]
	posts = Post.objects.filter(pk=path)
	hora = calcularHora(Post.objects.filter(pk=path))
	print(hora)
	return render(request, 'Club/ficha.html',{'posts':posts, 'hora':hora,})


def galeria(request):
    album = Albumes.objects.all()
    return render(request, 'Club/galeria.html',{'album':album})



def calcularHora(posts):
	hora=0
	minu=0
	hor = ""
	for i in posts:
		hora = i.fecha.hour+2
		minu = i.fecha.minute
	hor = str(hora)+":"+str(minu)
	return hor

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
   init_post = Post.objects.all().order_by("titulo")
   #Inicio el paginador
   pag = Paginador(request, init_post, 3, 'posts')
   n = 250
   cxt = {'posts': pag['posts'],
           'totPost': init_post,
           'paginator': pag,
          'n':n
          }
   return render_to_response('Club/post_list.html', context_instance=RequestContext(request, cxt))



def imagenes(request):
    a = Albumes.objects.all()
    return (request,'Club/galeria.html',{'a':a} )
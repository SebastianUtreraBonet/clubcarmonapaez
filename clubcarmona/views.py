from django.core.paginator import Paginator
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from datetime import datetime, date, time, timedelta
from clubcarmona.models import *
from django.core.mail import send_mail, EmailMessage
from .forms import FormularioContacto


def contactomail(request):
    formulario = FormularioContacto(initial={'comentario':' '})
    hoy = timezone.datetime.today()
    carreras = Carrera.objects.all().order_by('fecha')[0:10:]
    carrera = Carrera.objects.all().order_by('fecha')
    fail = "No se pudo enviar el email, compruebe que todos los campos estan rellenos correctamente."
    if request.method == 'POST':
        formulario = FormularioContacto(request.POST,initial={'comentario':'siiiii'})

        if formulario.is_valid():
            asunto = "INSCRIPCIÓN"
            mensaje =  "EMAIL: "+formulario.cleaned_data['email']\
                       +"\nDNI: "+formulario.cleaned_data['dni']\
                       +"\nNºSocio: "+str(formulario.cleaned_data['socio'])\
                       +"\n\nEvento: "+str(formulario.cleaned_data['evento'])\
                       +"\n\nComentario: "+formulario.cleaned_data['comentario']
            mail = EmailMessage(asunto, mensaje, to=['clubrafaelcarmonapaez@gmail.com'])
            mail.send()
            ok = "El email se ha enviado con exito."
            return render_to_response('Club/inscripcion.html',{'ok':ok, 'formulario':formulario,'hoy'     : hoy,
                                                       'carreras':carreras,
                                                       'carrera':carrera,}, context_instance=RequestContext(request))

        return render_to_response('Club/inscripcion.html',{'fail':fail,'formulario':formulario,'hoy'     : hoy,
                                                       'carreras':carreras,
                                                       'carrera':carrera,}, context_instance=RequestContext(request))
    return render_to_response('Club/inscripcion.html',{'formulario':formulario,
                                                       'hoy'     : hoy,
                                                       'carreras':carreras,
                                                       'carrera':carrera,}, context_instance=RequestContext(request))




def post_list1(request):
	post = Post.objects.all().order_by('fecha_publicacion')
	return render(request, 'Club/post_list.html', {'posts':post})

def calendario(request):
    hoy = timezone.datetime.today()
    carreras = Carrera.objects.all().order_by('fecha')
    mes = {1:"ENERO",2:"FEBRERO",3:"MARZO",4:"ABRIL",5:"MAYO",6:"JUNIO",7:"JULIO",8:"AGOSTO",9:"SEPTIEMBRE",int(10):"OCTUBRE",int(11):"NOVIEMBRE",int(12):"DICIEMBRE"}
    dias = timezone.datetime.today()+timedelta(days=20)
    d = timezone.datetime.today()+timedelta(days=5)
    return render(request, 'Club/calendario.html',{
            'hoy'     : hoy,
            'carreras':carreras,
            'mes':mes,
            'dias':dias,
            'd':d
    })


def carrera(request):
    path = request.path[9::]
    carrera = Carrera.objects.filter(pk=path)
    hora = calcularHora(Carrera.objects.filter(pk=path))
    d = timezone.datetime.today()+timedelta(days=5)
    hoy = timezone.datetime.today()
    carreras = Carrera.objects.all().order_by('fecha')[0:10:]
    carr = Carrera.objects.all().order_by('fecha')
    dias = timezone.datetime.today()+timedelta(days=20)
    return render(request, 'Club/carrera.html',{'carrera':carrera, 'hora':hora, 'd':d,
                                                'hoy'     : hoy,
                                                'carreras':carreras,
                                                'dias':dias,
                                                'carr':carr,})



def ficha(request):
    path = request.path[7::]
    posts = Post.objects.filter(pk=path)
    hora = calcularHora(Post.objects.filter(pk=path))
    print(hora)
    hoy = timezone.datetime.today()
    carreras = Carrera.objects.all().order_by('fecha')[0:10:]
    carrera = Carrera.objects.all().order_by('fecha')
    dias = timezone.datetime.today()+timedelta(days=20)
    return render(request, 'Club/ficha.html',{'posts':posts, 'hora':hora,
                                                'hoy'     : hoy,
                                                'carreras':carreras,
                                                'dias':dias,
                                                'carrera':carrera,})



def galeria(request):
    album = Albume.objects.all()
    hoy = timezone.datetime.today()
    carreras = Carrera.objects.all().order_by('fecha')[0:10:]
    carrera = Carrera.objects.all().order_by('fecha')
    dias = timezone.datetime.today()+timedelta(days=20)
    color = ['forestgreen','blueviolet','coral','deeppink','darkorange','darkgreen','crimson','deepskyblue']
    return render(request, 'Club/galeria.html',{'album':album,
                                                'color':color,
                                                'hoy'     : hoy,
                                                'carreras':carreras,

                                                'dias':dias,
                                                'carrera':carrera,})



def calcularHora(posts):
	hora=00
	minu=00
	hor = ""
	for i in posts:
		hora = i.fecha.hour+2
		minu = i.fecha.minute
	hor = str(hora)+":"+str(minu)
	return hor


def club(request):
    hoy = timezone.datetime.today()
    carreras = Carrera.objects.all().order_by('fecha')[0:10:]
    carrera = Carrera.objects.all().order_by('fecha')
    return render(request, 'Club/club.html',{
            'hoy'     : hoy,
            'carreras':carreras,
            'carrera':carrera,})





def participantes(request):
    hoy = timezone.datetime.today()
    carreras = Carrera.objects.all().order_by('fecha')[0:10:]
    carrera = Carrera.objects.all().order_by('fecha')
    participantes = Participante.objects.all()
    actualizado = max(Participante.objects.filter(fecha__lte=timezone.datetime.today()))
    return render(request, 'Club/participantes.html', {'participantes':participantes,
                                                       'actualizado':actualizado,
                                                       'hoy'     : hoy,
                                                        'carreras':carreras,
                                                        'carrera':carrera,})





def resultados(request):
    hoy = timezone.datetime.today()
    carreras = Carrera.objects.all().order_by('fecha').reverse()
    carreras2 = Carrera.objects.all().order_by('fecha')[0:10:]
    mes = {1:"ENERO",2:"FEBRERO",3:"MARZO",4:"ABRIL",5:"MAYO",6:"JUNIO",7:"JULIO",8:"AGOSTO",9:"SEPTIEMBRE",int(10):"OCTUBRE",int(11):"NOVIEMBRE",int(12):"DICIEMBRE"}
    dias = timezone.datetime.today()+timedelta(days=20)
    d = timezone.datetime.today()+timedelta(days=5)
    mes2 = calmes(mes)
    return render(request, 'Club/resultados.html',{
            'hoy'     : hoy,
            'carreras':carreras,
            'carreras2':carreras2,
            'mes2':mes2,
            'mes':mes,
            'dias':dias,
            'd':d
    })

def calmes(a):
    b=[]
    for i in a:

        b.append(i)
    b.reverse()
    print(b)
    return (b)


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
   carreras = Carrera.objects.all().order_by('fecha')[0:10:]
   carrera = Carrera.objects.all().order_by('fecha')
   mes = {1:"ENERO",2:"FEBRERO",3:"MARZO",4:"ABRIL",5:"MAYO",6:"JUNIO",7:"JULIO",8:"AGOSTO",9:"SEPTIEMBRE",int(10):"OCTUBRE",int(11):"NOVIEMBRE",int(12):"DICIEMBRE"}
   dias = timezone.datetime.today()+timedelta(days=20)
   init_post = Post.objects.all().order_by("fecha_publicacion").reverse()
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
            'carrera':carrera,
          }
   return render(request, 'Club/post_list.html',cxt)



def imagenes(request):
    a = Albume.objects.all()
    return (request,'Club/galeria.html',{'a':a} )


def biografia(request):
        hoy = timezone.datetime.today()
        carreras = Carrera.objects.all().order_by('fecha')[0:10:]
        carrera = Carrera.objects.all().order_by('fecha')
        return render(request, 'Club/biografia.html',{
            'hoy'     : hoy,
            'carreras':carreras,
            'carrera':carrera,})



def buscar(request):
    hoy = timezone.datetime.today()
    carreras = Carrera.objects.all().order_by('fecha')[0:10:]
    carrera2 = Carrera.objects.all().order_by('fecha')
    query = request.GET.get('buscar')
    if len(query) >= 1:

        carrera = Carrera.objects.filter(titulo__contains=query).__or__(Carrera.objects.filter(ciudad__contains=query)).order_by("fecha")
        post = Post.objects.filter(titulo__contains=query).order_by("fecha")
    else:
        carrera = ''
        post = ''
    

    return render(request, "Club/buscador.html", {

            'hoy'     : hoy,
            'carreras':carreras,
            'carrera':carrera2,
            "buscar2" : carrera,
            "buscar1": post,
            "query"   : query,})


from django.conf.urls import include, url
from clubcarmona import views


urlpatterns = [
    url(r'^$', views.post_list, name='home'),
    url(r'^calendario$', views.calendario, name='calendario'),
    url(r'^ficha/', views.ficha, name='ficha'),
    url(r'^carrera/', views.carrera, name='carrera'),
    url(r'^club$', views.club, name='club'),
    url(r'^galeria$', views.galeria, name='galeria'),
    url(r'^/?page', views.post_list),
	url(r'^static/img', views.imagenes, name='img'),
    url(r'^resultados', views.resultados, name='resultados'),
    url(r'^inscripcion', views.contactomail, name='inscripcion'),
    url(r'^listaparticipantes', views.participantes, name='participantes'),
    url(r'^buscar', views.buscar, name='buscar'),
    url(r'^club', views.biografia, name='club'),

]
from django.conf.urls import include, url
from clubcarmona import views

urlpatterns = [
    url(r'^$', views.post_list, name='home'),
    url(r'^calendario$', views.calendario, name='calendario'),
    url(r'^ficha', views.ficha, name='ficha'),
    url(r'^galeria$', views.galeria, name='galeria'),
    url(r'^/?page', views.post_list),
	url(r'^static/img', views.imagenes, name='img'),
    url(r'^resultados', views.resultados, name='resultados')
]
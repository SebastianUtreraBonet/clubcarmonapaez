from django.conf.urls import include, url
from clubcarmona import views

urlpatterns = [
    url(r'^$', views.post_list, name='home'),
    url(r'^calendario$', views.calendario, name='calendario'),
    url(r'^ficha', views.ficha, name='ficha'),
    url(r'^galeria$', views.galeria, name='galeria'),
    url(r'^calendario/',views.meses, name='meses'),
    url(r'^/?page', views.post_list)
]
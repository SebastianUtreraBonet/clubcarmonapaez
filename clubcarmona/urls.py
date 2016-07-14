from django.conf.urls import include, url
from clubcarmona import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^calendario$', views.calendario, name='calendario'),
    url(r'^ficha', views.ficha, name='ficha')

]
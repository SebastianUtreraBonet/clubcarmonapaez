from django.conf.urls import include, url
from clubcarmona import views

urlpatterns = [
    url(r'^$', views.post_list),
]
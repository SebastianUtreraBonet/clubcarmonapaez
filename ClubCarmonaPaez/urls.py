from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('clubcarmona.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

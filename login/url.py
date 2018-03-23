from django.conf.urls import patterns, url
from seguridad.views import Login

urlpatterns = patterns('',
                       url(r'^$', Login.as_view(), name="iniciar_sesion"),
                       )
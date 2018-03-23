from django.shortcuts import render
from django.views.generic import TemplateView

Importamos
la
vista
genérica
FormView
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
# Importamos el formulario de autenticación de django
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


# Create your views here.
class Login(FormView):
    # Establecemos la plantilla a utilizar
    template_name = 'inciar_session.html'
    # Indicamos que el formulario a utilizar es el formulario de autenticación de Django
    form_class = AuthenticationForm
    # Decimos que cuando se haya completado exitosamente la operación nos redireccione a la url menu de la aplicación login
    #success_url = reverse_lazy("login:menu")#

    def dispatch(self, request, *args, **kwargs):
        # Si el usuario está autenticado entonces nos direcciona a la url establecida en success_url
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        # Sino lo está entonces nos muestra la plantilla del login simplemente
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)
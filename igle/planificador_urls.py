from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView

from .planificador_views import YearView

urlpatterns = [
    
	url(r'^planificador(?P<anio>\d\d\d\d)$', YearView.as_view() ),
		
]

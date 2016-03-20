from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView

urlpatterns = [

	url(r'^geolocation$', TemplateView.as_view(template_name="xp/geolocation.html"), name="xp_geolocation"),
	url(r'^congregaciones$', TemplateView.as_view(template_name="xp/congregaciones.html"), name="xp_congregaciones"),

]

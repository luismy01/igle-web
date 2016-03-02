from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView

urlpatterns = [
    
	url(r'^$', 'igle.views.home_view', name="home"),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^personas/', include('personas.urls', namespace="personas", app_name="personas")),
	
	url(r'^login/$',  login, {"template_name": "igle/login.html"}, name="login"),
	url(r'^logout/$', logout, {"next_page": reverse_lazy("home")}, name="logout"),
	
	url(r'^index$',  login, {"template_name": "igle/index.html"}, name="index"),

	url(r'^xp/map/$', TemplateView.as_view(template_name="xp/map.html"), name="xp_map"),
	
	url(r'^', include('igle.planificador_urls', namespace="planificador")),
	
]

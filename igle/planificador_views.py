#from django.contrib.auth.decorators import login_required
#from django.core.urlresolvers import reverse_lazy
#from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
#from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
#from django.views.generic.list import BaseListView, MultipleObjectMixin

class YearView(TemplateView):
	
	template_name = "igle/planificador.html"
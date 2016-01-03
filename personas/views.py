from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView, View
from django.views.generic.list import BaseListView, MultipleObjectMixin

from .forms import PersonaForm
from .models import Persona
from .mixins import JSONResponseMixin, LoginRequiredMixin

import json

class PersonaListView(JSONResponseMixin, ListView):
	
	context_object_name = "personas"
	model = Persona
	paginate_by = 20
	template_name = "personas/list.html"
	
	def delete(self, request, *args, **kwargs):

		id_persona = kwargs["id"]

		p = Persona.objects.get(id=id_persona)
		p.delete()

		return JsonResponse(data={"result": "ok"}, safe=False)
		

	def get_context_data(self, **kwargs):

		context_data = super(PersonaListView, self).get_context_data(**kwargs)
		object_list = context_data["object_list"]
		queryset = self.get_queryset_as_dict(object_list)
		
		for item in queryset:
			item["fecha_nacimiento"] = str(item["fecha_nacimiento"])

		json_data = json.dumps(queryset)

		
		context_data["json_data"] = json_data

		return context_data

	
	def get_data(self, context):

		if "json_data" in context:
			return context["json_data"]
		else:
			return None
	
	
	def get_queryset_as_dict(self, queryset, *args, **kwargs):
		return [ model_to_dict(item) for item in queryset ]


	def post(self, request, *args, **kwargs):

		json_data = None
		CONTENT_TYPE = str(request.META["CONTENT_TYPE"])

		# content-type: application/json
		if "application/json" in CONTENT_TYPE:
			json_data = json.loads(request.read())

		# content-type: application/x-www-form-urlencoded
		if "model" in request.POST:

			json_data = json.loads(request.POST["model"])

		p = Persona()
		
		p.nombre = json_data["nombre"]
		p.email = json_data["email"]
		p.celular = json_data["celular"]
		p.fecha_nacimiento = json_data["fecha_nacimiento"]
		p.habilitado = json_data["habilitado"]
		p.genero = json_data["genero"]
		p.identificacion_tipo = json_data["identificacion_tipo"]
		p.identificacion_codigo = json_data["identificacion_codigo"]
		p.congregacion = json_data["congregacion"]
		
		p.save()
		json_data["id"] = p.id

		return JsonResponse(data=json_data, safe=False)


	def render_to_response(self, context):

		if self.request.GET.get('format') == 'json':
			return self.render_to_json_response(context, safe=False)
		else:
			return super(PersonaListView, self).render_to_response(context)
		

class PersonaSearchView(JSONResponseMixin, BaseListView):
	
	query_search = None
		
	def get(self, request, *args, **kwargs):
		self.query_search = ""
		return super(PersonaSearchView, self).get(request, *args, **kwargs)
		
	def get_queryset(self):
		
		queryset = None
		
		if self.query_search is None:
			queryset = Persona.objects.all()
		else:
			queryset = Persona.objects.filter(nombre__icontains=self.query_search)
			
		return queryset
	
	def render_to_response(self, context):
		return self.render_to_json_response(context, safe=False)
	
	
class PersonaEditView(LoginRequiredMixin, UpdateView):

	fields = ['nombre', 'identificacion_codigo', 'congregacion', 'fecha_nacimiento', 'email', 'celular', 'genero']
	model = Persona
	queryset = Persona.objects.all()
	template_name = "personas/persona_edit_form.html"
	slug_field = "id"
	
	
	def get(self, request, *args, **kwargs):

		print model_to_dict(self.get_object())

		return super(PersonaEditView, self).get(request, *args, **kwargs)


class PersonaDetailView(LoginRequiredMixin, DetailView):

	context_object_name = "persona"
	queryset = Persona.objects.all()
	template_name = "personas/persona_view_form.html"
	slug_field = "id"
	
	
	def get(self, request, *args, **kwargs):

		print model_to_dict(self.get_object())

		return super(PersonaDetailView, self).get(request, *args, **kwargs)



class PersonaCreateView(LoginRequiredMixin, CreateView):

	context_object_name = "persona"
	form_class = PersonaForm
	queryset = Persona.objects.all()
	template_name = "personas/persona_create_form.html"
	success_url = reverse_lazy('personas:list_view')
	
	
	def get(self, request, *args, **kwargs):
		return super(PersonaCreateView, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return super(PersonaCreateView, self).post(request, *args, **kwargs)
    
	def form_invalid(self, form):
		print "el formulaio no es valido"
		print form.errors
		return super(PersonaCreateView, self).form_invalid(form)
	
	def get_context_data(self, **kwargs):

		context_data = super(PersonaCreateView, self).get_context_data(**kwargs)
		form = context_data['form']
		
		persona = None
		
		if self.context_object_name in context_data:	
			persona = context_data[self.context_object_name]
		
		if persona is None:
			persona = Persona()
			persona.nombre = form['nombre'].value() if form['nombre'].value() is not None else persona.nombre
			persona.identificacion_codigo = form['identificacion_codigo'].value() if form['identificacion_codigo'].value() is not None else persona.identificacion_codigo
			persona.congregacion = form['congregacion'].value() if form['congregacion'].value() is not None else persona.congregacion
			persona.fecha_nacimiento = form['fecha_nacimiento'].value() if form['fecha_nacimiento'].value() is not None else persona.fecha_nacimiento
			persona.email = form['email'].value() if form['email'].value() is not None else persona.email
			persona.celular = form['celular'].value() if form['celular'].value() is not None else persona.celular

			context_data[self.context_object_name] = persona
		
		print form['fecha_nacimiento'].value()
		
		return context_data
	

class PersonaDeleteView(LoginRequiredMixin, DeleteView):
	
	model = Persona
	queryset = Persona.objects.all()
	slug_field = "id"
	success_url = reverse_lazy('personas:list_view')
	
	
	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)
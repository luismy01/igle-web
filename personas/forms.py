from django.forms import ModelForm
from .models import Persona

class PersonaForm(ModelForm):
	class Meta:
		model = Persona
		fields = ['nombre', 'identificacion_tipo', 'identificacion_codigo', 'congregacion', 'fecha_nacimiento', 'email', 'celular', 'genero', 'habilitado']
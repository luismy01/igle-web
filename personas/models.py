from django.core.urlresolvers import reverse
from django.db import models

class Persona(models.Model):

	GENERO_FEMENINO = "F"
	GENERO_MASCULINO = "M"
	GENERO_CHOICES = (
		(GENERO_FEMENINO, "Mujer"),
		(GENERO_MASCULINO, "Hombre"),
	)

	IDENTIFICACION_TIPO_CHOICES = (
		("CC", "Cedula de ciudadania"),
		("TI", "Tarjeta de identidad"),
		("PS", "Pasaporte"),
	)

	nombre = models.CharField(max_length=50)
	identificacion_tipo = models.CharField(max_length=3, choices=IDENTIFICACION_TIPO_CHOICES, default="CC")
	identificacion_codigo = models.CharField(max_length=30, db_index=True)
	congregacion = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	email = models.EmailField()
	celular = models.CharField(max_length=50)
	genero = models.CharField(max_length=3, choices=GENERO_CHOICES, default=GENERO_MASCULINO)
	habilitado = models.BooleanField(default=True)
	

	def __unicode__(self, *args, **kwargs):
		return self.nombre

	def get_absolute_url(self):
		return reverse('personas:detail_view', kwargs={"slug": self.id})

	def get_edit_url(self):
		return reverse('personas:edit_view', kwargs={"slug": self.id})

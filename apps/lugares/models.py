from django.db import models
from apps.ciudades.models import Ciudad

class Lugar(models.Model):
	ciudad = models.ForeignKey(Ciudad)
	nombre = models.CharField(max_length=150)
	descripcion = models.TextField(max_length=500)
	foto = models.ImageField(upload_to = 'img_lugar')

	def __str__(self):
		return self.nombre

	def traer_url_fotos_lugares(self):
		return 'http://localhost:8000/media/%s' % self.foto
		

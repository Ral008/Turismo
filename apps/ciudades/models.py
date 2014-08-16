from django.db import models

class Ciudad(models.Model):
	nombre = models.CharField(max_length=150)
	foto = models.ImageField(upload_to='img_ciudad')

	def __str__(self):
		return self.nombre

	def traer_url_fotos_ciudades(self):
		return 'http://localhost:8000/media/%s' % self.foto
	
		

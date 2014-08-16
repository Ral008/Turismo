from django.contrib import admin
from .models import Ciudad

class CiudadAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'imagen_portadas')
	#list_filter = ('autor',)
	search_fields = ('nombre','nombre')
	list_editable = ('nombre',)
	#filter_horizontal = ('autor',)

	def imagen_portadas(self, ciudad):
		url = ciudad.traer_url_fotos_ciudades()
		tag = "<img src='%s' height='65' width='85'>" % url
		return tag

	imagen_portadas.allow_tags = True	

admin.site.register(Ciudad,CiudadAdmin)

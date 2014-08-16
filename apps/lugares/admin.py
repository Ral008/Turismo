from django.contrib import admin
from .models import Lugar

class LugarAdmin(admin.ModelAdmin):
	list_display = ('id','nombre', 'descripcion', 'imagen_portadas')
	list_filter = ('ciudad',)
	search_fields = ('nombre','nombre')
	list_editable = ('nombre','descripcion')

	def imagen_portadas(self, lugar):
		url = lugar.traer_url_fotos_lugares()
		tag = "<img src='%s' height='65' width='85'>" % url
		return tag

	imagen_portadas.allow_tags = True

admin.site.register(Lugar,LugarAdmin)

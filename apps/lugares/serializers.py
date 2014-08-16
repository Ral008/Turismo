from rest_framework import serializers
from .models import Lugar

class LugarSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Lugar
		fileds = ('url', 'nombre', 'descripcion', 'ciudad', 'foto',)


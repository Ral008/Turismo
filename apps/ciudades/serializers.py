from rest_framework import serializers
from .models import Ciudad

class CiudadSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ciudad
		fileds = ('url', 'nombre', 'foto',)


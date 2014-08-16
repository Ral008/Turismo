from django.shortcuts import render
from .models import Ciudad
from .serializers import CiudadSerializer
from rest_framework import viewsets

class CiudadViewSet(viewsets.ModelViewSet):
	queryset = Ciudad.objects.all()
	serializer_class = CiudadSerializer

import json
from django.core import serializers
from django.http import HttpResponse

def getCiudades(request):
	#t = request.GET['test']
	#print(t)
	callback = request.GET.get('callback', '')
	ciudades = Ciudad.objects.all()	
	"""
	result = []
	for c in ciudades:
		diccionario = {}
		diccionario['id'] = c.id
		diccionario['nombre'] = c.nombre
		result.append(diccionario)
	
	response = json.dumps(result)
	response = callback + '(' + response + ');'
	return HttpResponse(response, content_type='application/json')  
	"""
	result = serializers.serialize('json', ciudades, fields=('nombre','foto'))
	result = callback + '(' + result + ');'
	return HttpResponse(result, content_type='application/json')	




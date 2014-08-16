from django.shortcuts import render
from .models import Lugar
from .serializers import LugarSerializer
from rest_framework import viewsets

class LugarViewSet(viewsets.ModelViewSet):
	queryset = Lugar.objects.all()
	serializer_class = LugarSerializer







import json
from django.core import serializers
from django.http import HttpResponse

def getLugares(request):
	idCiudad = request.GET['idCiudad']
	callback = request.GET.get('callback', '')
	lugares = Lugar.objects.filter(ciudad__id=idCiudad)		
	result = serializers.serialize('json', lugares, fields=('ciudad', 'nombre','descripcion', 'foto'))
	result = callback + '(' + result + ');'
	return HttpResponse(result, content_type='application/json')

def getUnLugar(request):
	idLugar = request.GET['idLugar']
	callback = request.GET.get('callback', '')
	unLugar = Lugar.objects.filter(id=idLugar)		
	result = serializers.serialize('json', unLugar, fields=('ciudad', 'nombre','descripcion', 'foto'))
	result = callback + '(' + result + ');'
	return HttpResponse(result, content_type='application/json')	
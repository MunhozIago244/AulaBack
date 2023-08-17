#importa as tabelas models que criamos
from .models import *
#importa os serializers que criamos
from .serializers import *
#importar a classe de configuração da API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import redirect

class PeopleAPIView(APIView):
    def post(self, request, *args, **kwargs):
        #recebe o json do cliente
        peopleJson = request.data
        peopleSerialized = PeopleSerializer(data=peopleJson)
        if peopleSerialized.is_valid():
            peopleSerialized.save()
            return Response(peopleSerialized.data, status=status.HTTP_201_CREATED)
        return Response(peopleSerialized.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, peopleId =''):
        if peopleId == '':
            #primeiro vamos fazer um select all do banco:
            peopleFound = People.objects.all() #select *from People;
            #agora pegamos os dados em python e mandamos p/ json
            peopleSerialized = PeopleSerializer(peopleFound, many=True)
            #manda a resposta para quem chamou a API:
            return Response(peopleSerialized.data)
        else: 
            try:        
                peopleFound = People.objects.get(id=peopleId)
                peopleSerialized = PeopleSerializer(peopleFound, many = False)
                return Response(peopleSerialized.data)
            except People.DoesNotExist:
                return Response(status= 404, data = 'People not found!!!')
        

class PlanetAPIView(APIView):
    def post(self, request, *args, **kwargs):
        #recebe o json do cliente
        planetJson = request.data
        planetSerialized = PlanetSerializer(data=planetJson)
        if planetSerialized.is_valid():
            planetSerialized.save()
            return Response(planetSerialized.data, status=status.HTTP_201_CREATED)
        return Response(planetSerialized.errors, status=status.HTTP_400_BAD_REQUEST) 
    def get(self, request, planetsId =''):
        if planetsId == '':
            #primeiro vamos fazer um select all do banco:
            planetFound = Planet.objects.all() #select *from Planet;
            #agora pegamos os dados em python e mandamos p/ json
            planetSerialized = PlanetSerializer(planetFound, many=True)
            #manda a resposta para quem chamou a API:
            return Response(planetSerialized.data)
        else: 
            try:
                planetFound = Planet.objects.get(id=planetsId)
                planetSerialized = PlanetSerializer(planetFound, many = False)
                return Response(planetSerialized.data)
            except Planet.DoesNotExist:
                return Response(status= 404, data='Planet not found!!!')
        
        
class StarshipsAPIView(APIView):
    def post(self, request, *args, **kwargs):
        #recebe o json do cliente
        starshipJson = request.data
        starshipSerialized = StarshipsSerializer(data=starshipJson)
        if starshipSerialized.is_valid():
            starshipSerialized.save()
            return Response(starshipSerialized.data, status=status.HTTP_201_CREATED)
        return Response(starshipSerialized.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, starshipsId =''):
        if starshipsId == '':
            #primeiro vamos fazer um select all do banco:
            starshipsFound = Starships.objects.all() #select *from Starships;
            #agora pegamos os dados em python e mandamos p/ json
            starshipsSerialized = StarshipsSerializer(starshipsFound, many=True)
            #manda a resposta para quem chamou a API:
            return Response(starshipsSerialized.data)
        else: 
            try:
                starshipsFound = Starships.objects.get(id=starshipsId)
                starshipsSerialized = StarshipsSerializer(starshipsFound, many = False)
                return Response(starshipsSerialized.data)
            except Starships.DoesNotExist:
                return Response(status= 404, data='Starships not found!!!')
        
        

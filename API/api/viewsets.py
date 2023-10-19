# Importando as viwes sets
from rest_framework import viewsets 
from API.api import serializers
from API import models
from django_filters.rest_framework import DjangoFilterBackend
# import django_filters.rest_framework

# Views Sets para os modelos de dados
class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FeedbackSerializer
    queryset = models.Feedback.objects.all()#todos os campos dos models, ou seja, todos os objetos

class PlataformaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PlataformaSerializer
    queryset = models.Plataforma.objects.all()

class OuvidoriaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OuvidoriaSerializer
    queryset = models.Ouvidoria.objects.all()

class FeedbackByPlataformaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PlataformaSerializer
    queryset = models.Plataforma.objects.all()
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id', 'nome'] # Filtro pelo nome e pelo 'id'
    # filterset_fields = ['nome'] # Filtragem pelo nome
    filterset_fields = ['id'] # Filtragem pelo id
    
class OuvidoriaByPlataformaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OuvidoriaSerializer
    queryset = models.Ouvidoria.objects.all()
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id', 'nome'] # Filtro pelo nome e pelo 'id'
    # filterset_fields = ['nome'] # Filtragem pelo nome
    filterset_fields = ['id'] # Filtragem pelo id
    
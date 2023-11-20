# Importando as viwes sets
from rest_framework import viewsets
from API.api import serializers
from API import models
from django_filters.rest_framework import DjangoFilterBackend

# Views Sets para os modelos de dados
# Criação de um feedback
class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FeedbackSerializer
    queryset = models.Feedback.objects.all()#todos os campos dos models, ou seja, todos os objetos

# Metodo post de plataforma
class PlataformaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PlataformaSerializer
    queryset = models.Plataforma.objects.all()

# Metodo post de Ouvidoria
class OuvidoriaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OuvidoriaSerializer
    queryset = models.Ouvidoria.objects.all()

# Metodo get de Feedback por plataforma
class FeedbackByPlataformaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.FeedbackbyPlataformaSerializer
    queryset = models.Plataforma.objects.all()
    # queryset = models.Feedback.objects.filter(tipo_de_plataforma = PlataformaViewSet) 
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id'] # Filtragem pelo id
# Metodo Get para feedback  
class FeedbackGetViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.FeedbackgetSerializer
    queryset = models.Feedback.objects.all()
    
    
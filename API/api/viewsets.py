from rest_framework import viewsets # Importando as viwes sets
from API.api import serializers
from API import models

class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FeedbackSerializer
    queryset = models.Feedback.objects.all()#todos os campos dos models, ou seja, todos os objetos


class PlataformaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PlataformaSerializer
    queryset = models.Plataforma.objects.all()
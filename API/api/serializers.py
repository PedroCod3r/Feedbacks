from rest_framework import serializers # Importando o rest
from API import models # Importanto o models

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = '__all__'

class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Plataforma
        fields = '__all__'
        
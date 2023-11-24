from rest_framework import serializers # Importando o rest
from API.models import Feedback, Ouvidoria, Plataforma  # Importanto o models

class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = ['nome']

class OuvidoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ouvidoria
        fields = ['nome']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id','plataforma', 'ouvidoria', 'mensagem_digitada_na_ouvidoria', 'data_criacao_ouvidoria']

    plataforma = PlataformaSerializer(source = 'tipo_de_plataforma', read_only= True)


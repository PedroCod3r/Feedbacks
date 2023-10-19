from rest_framework import serializers # Importando o rest
from API import models # Importanto o models

class PlataformaSerializer(serializers.ModelSerializer):
    feedbacks_plataforma = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='mensagem_digitada_na_ouvidoria'
    )
    class Meta:
        model = models.Plataforma
        # fields = ['nome', 'inativo', 'feedbacks_plataforma']
        fields = '__all__'
class OuvidoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ouvidoria
        fields = '__all__'
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        # fields = ['data_criacao_ouvidoria', 'mensagem_digitada_na_ouvidoria', 'tipo_de_plataforma', 'tipo_de_plataforma.nome']
        fields = '__all__'

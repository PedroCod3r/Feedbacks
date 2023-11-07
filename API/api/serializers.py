from rest_framework import serializers # Importando o rest
from API import models # Importanto o models

class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Plataforma
        fields = '__all__'
class OuvidoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ouvidoria
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = '__all__'

class FeedbackbyPlataformaSerializer(serializers.ModelSerializer):
    # Retornar os feedbacks por plataforma
    # tipo_de_feedback = FeedbackSerializer(read_only=True)
    # feedbacks_plataforma = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='mensagem_digitada_na_ouvidoria'
    # )
    tipo_de_ouvidoria = OuvidoriaSerializer(read_only=True)
    tipo_de_feedback = FeedbackSerializer(read_only=True)
    class Meta:
        model = models.Plataforma
        # fields = ['id', 'nome', 'inativo', 'tipo_de_feedback']
        fields = '__all__'
class FeedbackgetSerializer(serializers.ModelSerializer):
    # Retorna dentro do JSON o nome e o status do tipo de plataforma e tipo de ouvidoria
    tipo_de_plataforma = PlataformaSerializer(read_only=True)
    tipo_de_ouvidoria = OuvidoriaSerializer(read_only=True)
    class Meta:
        model = models.Feedback
        fields = ['id','tipo_de_plataforma', 'tipo_de_ouvidoria', 'mensagem_digitada_na_ouvidoria' ,'data_criacao_ouvidoria']

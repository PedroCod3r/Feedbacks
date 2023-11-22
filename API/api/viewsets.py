# Importando as viwes sets
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
# Import models
from API.models import Feedback, Plataforma, Ouvidoria
# Import serializer
# from API.api import FeedbackSerializer
from .serializers import FeedbackSerializer, PlataformaSerializer, OuvidoriaSerializer
# Views Sets para os modelos de dados
# Criação de um feedback


@api_view(http_method_names= ['GET','POST'])
def createFeedback(request):
    if request.method == "GET":
        feedback = Feedback.objects.filter(tipo_de_plataforma__inativo = False)
        serializers = FeedbackSerializer(instance=feedback, many=True)
        return Response(serializers.data)
    
    if request.method == "POST":
        serializers = FeedbackSerializer(data=request.data)
        serializers.is_valid()
        serializers.save()
        return Response({'message': 'feedback created'}, status=status.HTTP_201_CREATED)
        
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET'])
def listPlataforms(request):
    # if request.method == "GET":
        plataforma = Plataforma.objects.filter(inativo = False)
        serializer = PlataformaSerializer(instance=plataforma, many= True)
        return Response(serializer.data)

@api_view(http_method_names=['GET'])
def listOuvidoria(request):
    # if request.method == "GET":
        ouvidoria = Ouvidoria.objects.filter(inativo = False)
        serializer = OuvidoriaSerializer(instance=ouvidoria, many= True)
        return Response(serializer.data)

# @api_view(http_method_names=['GET'])
# def feedByPlataform(request):
    #   if request.method == "GET":
    # plataforma = Plataforma.objects.filter(id = id)
    # feed = Feedback.objects.all()
    # serializer = FeedbackSerializer(instance=feed, many=True)
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id', 'nome']
    # return Response(serializer.data)
    
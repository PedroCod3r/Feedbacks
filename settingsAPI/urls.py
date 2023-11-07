# Iniciando as importações
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from API.api import viewsets

# Registrando rotas
route = routers.DefaultRouter()
route.register('feedbacks/filter', viewsets.FeedbackByPlataformaViewSet, basename='FeedbackByPlataforma')
# route.register('feedbacks/ouvidoria', viewsets.FeedbackByOuvidoriaViewSet, basename='OuvidoriaByPlataforma')
route.register('feedbacks/get', viewsets.FeedbackGetViewSet, basename='Feedback')
route.register('feedbacks', viewsets.FeedbackViewSet, basename='Feedback')
route.register('plataforma', viewsets.PlataformaViewSet, basename='Plataforma')
route.register('ouvidoria', viewsets.OuvidoriaViewSet, basename='Ouvidoria')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]

# Iniciando as importações
from django.contrib import admin
from django.urls import path
from API.api.viewsets import createFeedback, listPlataforms, listOuvidoria

# Registrando rotas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/feeds/',createFeedback),
    path('api/plataformas/',listPlataforms),
    # path('api/feedback/plataforma/', feedByPlataform),
    path('api/ouvidorias/',listOuvidoria),
]

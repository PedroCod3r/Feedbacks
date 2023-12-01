# Iniciando as importações
from django.contrib import admin
from django.urls import path
from API.api.views import createFeedback, listPlataforms, feedByOuvidoria, feedByPlataform, listOuvidoria

# Registrando rotas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/feeds/',createFeedback),
    path('api/plataformas/',listPlataforms),
    path('api/feedbyplataforma/<int:plataforma_id>/', feedByPlataform),
    path('api/ouvidorias/',listOuvidoria),
    path('api/feedbyouvidoria/<int:ouvidoria_id>/',feedByOuvidoria),
]

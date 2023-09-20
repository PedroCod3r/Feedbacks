"""settingsAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from library.views import home

from rest_framework import routers


from API.api import viewsets

route = routers.DefaultRouter()

route.register('feedbacks', viewsets.FeedbackViewSet, basename='Feedbacks')
route.register('plataforma', viewsets.PlataformaViewSet, basename='plataforma')
# route.get('feedbacks', home)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    # path('', home, name='index'),
]

from django.db import models

# Create your models here.
class Plataforma(models.Model):
    nome = models.CharField(max_length=50)
    inativo = models.BooleanField(default=False)

class Ouvidoria(models.Model):
    nome = models.CharField(max_length=50)
    inativo = models.BooleanField(default=False)

class Feedback(models.Model):
    tipo_de_plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE) 
    tipo_de_ouvidoria = models.ForeignKey(Ouvidoria, on_delete=models.CASCADE)
    mensagem_digitada_na_ouvidoria = models.CharField(max_length=255)
    data_criacao_ouvidoria = models.DateTimeField(auto_now_add=True)
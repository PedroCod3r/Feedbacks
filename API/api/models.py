from django.db import models

# Create your models here.
    
class Plataforma(models.Model):
    nome = models.CharField(max_length=50)
    inativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Ouvidoria(models.Model):
    nome = models.CharField(max_length=50)
    inativo = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome

class Feedback(models.Model):
    tipo_de_plataforma = models.ForeignKey(Plataforma, related_name='feedbacks_plataforma', on_delete=models.CASCADE, null=True)
    tipo_de_ouvidoria = models.ForeignKey(Ouvidoria, related_name='feedbacks_ouvidoria', on_delete=models.CASCADE)
    mensagem_digitada_na_ouvidoria = models.CharField(max_length=255)
    data_criacao_ouvidoria = models.DateTimeField(auto_now_add=True)

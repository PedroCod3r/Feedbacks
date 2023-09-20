from django.contrib import admin
from .models import Feedback, Plataforma, Ouvidoria
# Register your models here.
admin.site.register([
    Feedback,
    Plataforma,
    Ouvidoria,
])
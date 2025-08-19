from django.contrib import admin
from . import views





urlpatterns = [
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    
]







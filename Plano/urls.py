from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_plano, name='criar_plano'),
    path('plano/<int:id>/', views.exibir_plano, name='exibir_plano'),
    path('listar/', views.listar_planos, name='listar_planos'),
]

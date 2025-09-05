from django.urls import path
from . import views

urlpatterns = [
    path('consultar/', views.consultar_site, name='consultar_site'),
    path('consulta/<int:id>/', views.exibir_consulta, name='exibir_consulta'),
    path('listar/', views.listar_consultas, name='listar_consultas'),
]
""
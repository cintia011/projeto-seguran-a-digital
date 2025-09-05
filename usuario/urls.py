from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_usuario, name='criar_usuario'),
    path('perfil/<int:id>/', views.exibir_usuario, name='exibir_usuario'),
    path('login/', views.login_usuario, name='login'),
]

from django.shortcuts import render
from django.shortcuts import render

# Página inicial
def home(request):
    return render(request, 'home.html')

# Página criar usuário
def criar_usuario(request):
    return render(request, 'usuario/criar_usuario.html')

# Página exibir usuário
def exibir_usuario(request):
    usuario = {"nome": "João", "email": "joao@email.com"}  # Exemplo
    return render(request, 'usuario/exibir_usuario.html', {"usuario": usuario})

# Página de login
def login_view(request):
    return render(request, 'usuario/login.html')

# Create your views here.

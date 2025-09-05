from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def home_view(request):
    return render(request, 'home.html')


def criar_usuario(request):
    return render(request, 'Usuario/criar_usuario.html')

def exibir_usuario(request, id):
    return render(request, 'Usuario/exibir_usuario.html', {'id': id})

def login_usuario(request):
    return render(request, 'Usuario/login.html')

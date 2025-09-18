from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render

<<<<<<< HEAD
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
=======
# Create your views here.
>>>>>>> e526451f680b9632532d6e0a157a1b0f12702170

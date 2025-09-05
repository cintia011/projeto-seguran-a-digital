from django.shortcuts import render

def criar_plano(request):
    return render(request, 'Plano/criar_plano.html')

def exibir_plano(request, id):
    return render(request, 'Plano/exibir_plano.html', {'id': id})

def listar_planos(request):
    return render(request, 'Plano/listar_planos.html')

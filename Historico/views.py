from django.shortcuts import render

def consultar_site(request):
    return render(request, 'Historico/consultar_site.html')

def exibir_consulta(request, id):
    return render(request, 'Historico/exibir_consulta.html', {'id': id})

def listar_consultas(request):
    return render(request, 'Historico/listar_consultas.html')

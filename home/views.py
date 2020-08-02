from django.shortcuts import render
from .models import Servico, Informacao

# Create your views here.

def home(request):
    servicos = Servico.objects.all()
    info = Informacao.objects.all()

    for iterar in info:
        telefone = iterar.telefone
        email = iterar.email
        slogan = iterar.slogan
        endereco = iterar.endereco
        nomeLugar = iterar.nomeLugar
        frase = iterar.frase
    return render(request, 'index.html', {'dados': servicos, 'info': info, 'telefone':telefone, 'email':email,'slogan':slogan, 'endereco':endereco, 'nomeLugar':nomeLugar,'frase':frase})
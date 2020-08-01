from django.shortcuts import render
from .models import Servico, Informacao

# Create your views here.

def home(request):
    servicos = Servico.objects.all()
    info = Informacao.objects.all()

    return render(request, 'index.html', {'dados': servicos, 'info': info})
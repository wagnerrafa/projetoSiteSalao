from django.shortcuts import render
from .models import Servico, MinhaInformacao, Cliente, Promo
from django.core.mail import EmailMessage
from django.utils.safestring import mark_safe
from django.http import HttpResponse

def home(request):
    msgConfirm = " "
    response = "a"
    telefone = " "
    email = " "
    slogan = " "
    endereco = " "
    nomeLugar = ""
    frase = ""
    instagram = ""
    foto = ""
    logo = ""
    fotoFundo = ""
    promo = ""
    info = ""
    servicos = "a"
    contPromo = ""
    
    if request.method == 'POST':
        pessoa = Cliente()
        pessoa.nome = request.POST['nome']
        pessoa.telefone = request.POST['tel']
        pessoa.email = request.POST['email']
        pessoa.date = request.POST['date']
        pessoa.servico = request.POST['servico']
        pessoa.save()
        
        filtrarData = pessoa.date
        filtrarData = filtrarData.split('-')
        ano= filtrarData[0]
        mes = filtrarData[1]
        dia = filtrarData[2]
        filtrarData1 = dia.split('T')
        dia = filtrarData1[0]
        hora = filtrarData1[1]
        data = dia+"/"+mes+"/"+ano

        msgConfirm = "Obrigado "+pessoa.nome+", o serviço de "+pessoa.servico+" foi marcado para o dia "+data+" ás "+hora+". Qualquer dúvida entre em contato pelo telefone "+telefone
        
        msgMe = pessoa.nome+" agendou o serviço de "+pessoa.servico+" para o dia "+data+" ás "+hora+" Telefone de contato "+pessoa.telefone+" Email de contato "+pessoa.email
        
        emailUser = EmailMessage('Agendamento',mark_safe(msgConfirm), to=[pessoa.email])
        emailUser.send()
        email = EmailMessage('Novo agendamento',mark_safe(msgMe), to=[email])
        email.send()
        response = HttpResponse()
        response = response.status_code


        

    return render(request, 'index.html', {'dados': servicos, 'info': info, 'telefone':telefone, 'email':email,'slogan':slogan, 'endereco':endereco, 'nomeLugar':nomeLugar,'frase':frase,'msgConfirm':msgConfirm,'instagram':instagram,'foto':foto,'logo':logo,'fotoFundo':fotoFundo,'promo':promo,'contPromo':contPromo,'response':response})


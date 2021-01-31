from django.shortcuts import render
from .models import Servico, MinhaInformacao, Cliente, Promo
from django.core.mail import EmailMessage
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import os
def home(request):
    cliente = Cliente.objects.filter(id=1).values()
    print(cliente)
    if "wagner_rafa@hotmail.com.br" in cliente[0]['email']:
        print('id\n')
    for x in cliente:
        if "wagner_rafa@hotmail.com.br" in x:
            print(x,'x\n')
    msgConfirm = ""
    response = "a"
    contServicos = 0
    if Servico.objects.all():
        servicos = Servico.objects.all()
        contServicos = servicos.count
    else:
        servicos = "a"

    if MinhaInformacao.objects.all():
        info = MinhaInformacao.objects.all()
        for iterar in info:
            telefone = iterar.telefone
            email = iterar.email
            slogan = iterar.slogan
            endereco = iterar.endereco
            nomeLugar = iterar.nomeLugar
            frase = iterar.frase
            instagram = iterar.instagram
            foto = iterar.foto
            logo = iterar.logo
    else:
        info = ""
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
    if Promo.objects.all():
        promo = Promo.objects.all()
        contPromo = len(promo)

    else:
        promo = ""
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

        msgConfirm = 'Obrigado '+pessoa.nome+'\n\no serviço de '+pessoa.servico+' foi marcado para o dia '+data+' ás '+hora+'\n\nQualquer dúvida entre em contato pelo telefone '+telefone+'\n\nAtenciosamente, \n'+nomeLugar
        msgMe = "Olá "+nomeLugar+"\n\n"+pessoa.nome+" agendou o serviço de "+pessoa.servico+" para o dia "+data+" ás "+hora+"\nTelefone de contato "+pessoa.telefone+"\nEmail de contato\n"+pessoa.email
        
        emailUser = EmailMessage('Agendamento',mark_safe(msgConfirm), to=[pessoa.email])
        email = EmailMessage('Novo agendamento',mark_safe(msgMe), to=[email])
        #emailUser.send()
        #email.send()
        response = HttpResponse()
        response = response.status_code

    return render(request, 'index.html/', {'dados': servicos, 'info': info, 'telefone':telefone, 'email':email,'slogan':slogan, 'endereco':endereco, 'nomeLugar':nomeLugar,'frase':frase,'msgConfirm':msgConfirm,'instagram':instagram,'foto':foto,'logo':logo,'promo':promo,'contPromo':contPromo,'response':response, 'contServicos': contServicos})


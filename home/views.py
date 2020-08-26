from django.shortcuts import render
from .models import Servico, MinhaInformacao, Cliente, Promo
from django.core.mail import EmailMessage
from django.utils.safestring import mark_safe

def home(request):
    servicos = Servico.objects.all()
    info = MinhaInformacao.objects.all()
    promo = Promo.objects.all()
    msgConfirm = " "
    contPromo = len(promo)

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
        fotoFundo = iterar.fotoFundo
    
    if request.method == 'POST':
        pessoa = Post()
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
        
    return render(request, 'index.html', {'dados': servicos, 'info': info, 'telefone':telefone, 'email':email,'slogan':slogan, 'endereco':endereco, 'nomeLugar':nomeLugar,'frase':frase,'msgConfirm':msgConfirm,'instagram':instagram,'foto':foto,'logo':logo,'fotoFundo':fotoFundo,'promo':promo,'contPromo':contPromo})


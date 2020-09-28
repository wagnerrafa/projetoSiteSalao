from django.db import models
from cloudinary.models import CloudinaryField

class Servico(models.Model):
    servico = models.CharField(
        max_length=50,
        verbose_name='servico'
    )
    descricao = models.CharField(
        max_length=255,
        verbose_name='descricao'
    )
    upload = CloudinaryField('Foto do serviço')
    def __str__(self):
        return(self.servico)

class MinhaInformacao(models.Model):
    telefone = models.CharField(
        max_length=20,
        verbose_name='Telefone'
        )
    email = models.EmailField(
        max_length=100,
        verbose_name= 'Email'
        )
    endereco = models.CharField(
        max_length=255,
        verbose_name='Endereço'
        )
    slogan = models.CharField(
        max_length=255,
        verbose_name='Slogan'
        )
    nomeLugar = models.CharField(
        max_length=50,
        verbose_name='Nome do lugar'
        )
    frase = models.CharField(
        max_length=255,
        verbose_name='Frase do logo'
        )
    instagram = models.CharField(
        max_length=50,
        verbose_name='Nome do usúario Instagram',
        )
    foto = CloudinaryField('Foto da capa')
    logo = CloudinaryField('Foto do logo')

    def __str__(self):
        return(self.nomeLugar)
    class Meta:
            verbose_name_plural = 'Minhas informações'
class Cliente(models.Model):
    if Servico.objects.all():
        dados = Servico.objects.all()
        Servico1 = []
        Servico2 = []
        for dado in dados:
            Servico2 = Servico1.append(dado)
        Servico = Servico2
    else:
        Servico = ""
    nome = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )
    telefone = models.CharField(
        max_length=20,
        verbose_name='Telefone'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Email'
    )
    date = models.CharField(
        max_length=20,
        verbose_name='Data da sessão'
    )
    servico = models.CharField(
        max_length=50,
        verbose_name='Servico',
        choices=Servico
    )
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return(self.nome)

class Promo(models.Model):
    imagemPromo = CloudinaryField('Foto da Promoção')
    tituloPromo = models.CharField(
        max_length=50,
        verbose_name='Titulo da Promoção',
    )
    descPromo = models.CharField(
        max_length=255,
        verbose_name='Descrição com detalhes da promoção',
    )
    dataDuracao = models.DateField(
        verbose_name='Data final da Promoção',
    )
    dataCriacao = models.DateField(auto_now_add=True)
    def __str__(self):
        return(self.tituloPromo)
    class Meta:
        verbose_name_plural = 'Promoções'

class Report(models.Model):

    choices = (
        ( "agenda" , "Agenda Completa"),
        ( "nome" , "nome" ),
        ( "telefone" , "telefone" ),
        ( "email" , "email"),
        ( "servico" , "servico"),
    )
    
    date = models.DateField('Data', auto_now_add=True)
    choice = models.CharField('Filtrar por',max_length = 255, choices = choices
    )
    
    nomePesquisa = models.CharField('Coloque a pesquisa', max_length=100)
    def __str__(self):
        return self.nomePesquisa
    
    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendamentos'
        ordering = ['-id']
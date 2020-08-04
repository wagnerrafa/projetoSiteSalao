from django.db import models

class Servico(models.Model):
    servico = models.CharField(
        max_length=50,
        verbose_name='servico')
    descricao = models.CharField(
        max_length=255,
        verbose_name='descricao')
    upload = models.ImageField(upload_to='media/upload/')

class Informacao(models.Model):
    telefone = models.CharField(
        max_length=20,
        verbose_name='Telefone')
    email = models.EmailField(
        max_length=100,
        verbose_name= 'Email')
    endereco = models.CharField(
        max_length=255,
        verbose_name='Endereço')
    slogan = models.CharField(
        max_length=255,
        verbose_name='Slogan')
    nomeLugar = models.CharField(
        max_length=255,
        verbose_name='Nome do lugar')
    frase = models.CharField(
        max_length=255,
        verbose_name='Frase do logo'
    )

class Post(models.Model):
    dados = Servico.objects.all()
    Servico1 = []
    Servico2 = []
    for dado in dados:
        Servico2 = Servico1.append(dado)
    Servico = Servico2
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
        max_length=255,
        verbose_name='Data da sessão'
    )
    servico = models.CharField(
        max_length=255,
        verbose_name='Servico',
        choices=Servico
    )
    created_at = models.DateField(auto_now_add=True)
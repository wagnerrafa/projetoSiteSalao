from django.db import models

class Servico(models.Model):
    servico = models.CharField(
        max_length=50,
        verbose_name='servico',
        default="Nome do serviço")
    descricao = models.CharField(
        max_length=255,
        verbose_name='descricao',
        default="Descricao")
    upload = models.ImageField(upload_to='media/upload/',verbose_name='Foto do serviço')

class MinhaInformacao(models.Model):
    telefone = models.CharField(
        max_length=20,
        verbose_name='Telefone',
        default="0")
    email = models.EmailField(
        max_length=100,
        verbose_name= 'Email',
        default="exemplo@gmail.com")
    endereco = models.CharField(
        max_length=255,
        verbose_name='Endereço',
        default="rua 0")
    slogan = models.CharField(
        max_length=255,
        verbose_name='Slogan',
        default="Aqui vai o slogan")
    nomeLugar = models.CharField(
        max_length=50,
        verbose_name='Nome do lugar',
        default="Aqui é o nome do lugar")
    frase = models.CharField(
        max_length=255,
        verbose_name='Frase do logo',
        default="Aqui é a frase de efeito"
    )
    instagram = models.CharField(
        max_length=50,
        verbose_name='Nome do usúario Instagram',
        default="Aqui é o seu instagram"
    )
    foto = models.ImageField(upload_to='media/upload/',verbose_name='Foto de capa', )
    logo = models.ImageField(upload_to='media/upload/',verbose_name='Logo')
    fotoFundo = models.ImageField(upload_to='media/upload/',verbose_name='Foto de fundo da pagina')

class Cliente(models.Model):
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
    
    created_at = models.DateField(auto_now_add=True)

class Promo(models.Model):
    imagemPromo = models.ImageField(upload_to='media/upload/',verbose_name='Foto da Promoção')
    tituloPromo = models.CharField(
        max_length=50,
        verbose_name='Titulo da Promoção',
        default="Titulo da promocao "
    )
    descPromo = models.CharField(
        max_length=255,
        verbose_name='Descrição com detalhes da promoção',
        default="Descricao da promocao"
    )
    dataDuracao = models.DateField(
        verbose_name='Data final da Promoção',
        default="Data duracao"
    )
    dataCriacao = models.DateField(auto_now_add=True)

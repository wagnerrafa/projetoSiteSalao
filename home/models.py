from django.db import models

class Servico(models.Model):
    servico = models.CharField(
        max_length=50,
        verbose_name='servico')
    descricao = models.CharField(
        max_length=255,
        verbose_name='descricao')
    upload = models.ImageField(upload_to='media/upload/',verbose_name='Foto do serviço')

class MinhaInformacao(models.Model):
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
        max_length=50,
        verbose_name='Nome do lugar')
    frase = models.CharField(
        max_length=255,
        verbose_name='Frase do logo'
    )
    instagram = models.CharField(
        max_length=50,
        verbose_name='Nome do usúario Instagram'
    )
    foto = models.ImageField(upload_to='media/upload/',verbose_name='Foto de capa')
    logo = models.ImageField(upload_to='media/upload/',verbose_name='Logo')
    fotoFundo = models.ImageField(upload_to='media/upload/',verbose_name='Foto de fundo da pagina')

class Cliente(models.Model):
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
        max_length=20,
        verbose_name='Data da sessão'
    )
    servico = models.CharField(
        max_length=50,
        verbose_name='Servico',
        choices=Servico
    )
    created_at = models.DateField(auto_now_add=True)

class Promo(models.Model):
    imagemPromo = models.ImageField(upload_to='media/upload/',verbose_name='Foto da Promoção')
    tituloPromo = models.CharField(
        max_length=50,
        verbose_name='Titulo da Promoção'
    )
    descPromo = models.CharField(
        max_length=255,
        verbose_name='Descrição com detalhes da promoção'
    )
    dataDuracao = models.DateField(
        verbose_name='Data final da Promoção'
    )
    dataCriacao = models.DateField(auto_now_add=True)

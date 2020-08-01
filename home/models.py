from django.db import models

# Create your models here.

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
        verbose_name='telefone')
    email = models.EmailField(
        max_length=100,
        verbose_name= 'email')
    endereco = models.CharField(
        max_length=255,
        verbose_name='endereco')
    slogan = models.CharField(
        max_length=255,
        verbose_name='slogan')
    nomeLugar = models.CharField(
        max_length=255,
        verbose_name=' nome do lugar')


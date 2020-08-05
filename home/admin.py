from django.contrib import admin
from .models import Servico, MinhaInformacao, Cliente

admin.site.register(MinhaInformacao)
admin.site.register(Servico)
admin.site.register(Cliente)

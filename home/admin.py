from django.contrib import admin
from .models import Servico, MinhaInformacao, Cliente, Promo, Report
import xlwt
from django.contrib.auth.models import User

from weasyprint import HTML
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django_object_actions import DjangoObjectActions

admin.site.register(MinhaInformacao)
admin.site.register(Servico)
admin.site.register(Cliente)
admin.site.register(Promo)

@admin.register(Report)
class ReportAdmin(DjangoObjectActions, admin.ModelAdmin):
    
    def export_users_xls(self , request, obj):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        
        columns = ['Nome', 'Telefone', 'Email', 'Data','Servico', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        name = obj.nomePesquisa

        if obj.choice == "telefone":
            rows = Cliente.objects.filter(telefone__icontains=name).values_list('nome', 'telefone', 'email', 'date','servico')
        elif obj.choice == "email":
            rows = Cliente.objects.filter(email__icontains=name).values_list('nome', 'telefone', 'email', 'date','servico')
        elif obj.choice == "nome":
            rows = Cliente.objects.filter(nome__icontains=name).values_list('nome', 'telefone', 'email', 'date','servico')
        elif obj.choice == "servico":
            rows = Cliente.objects.filter(servico__icontains=name).values_list('nome', 'telefone', 'email', 'date','servico')
        else:
            rows = Cliente.objects.all().values_list('nome', 'telefone', 'email', 'date','servico')
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response

    export_users_xls.label = 'Gerar excel'
    export_users_xls.short_description = 'Clique para gerar o EXCEl dessa ordem de serviço'

    change_actions = ('export_users_xls',)

    

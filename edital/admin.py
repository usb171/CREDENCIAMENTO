from django.contrib import admin
from .models import *
from core.models import Documento


class DocumentoInline(admin.StackedInline):
    model = Documento
    extra = 0


class EditalAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'status', 'data_publicacao', 'inicio_inscricao', 'fim_inscricao']
    list_filter = ['status']
    filter_horizontal = ('contratante', 'servicos')
    inlines = [DocumentoInline]



class DocumentoRequisitoInscricaoInline(admin.StackedInline):
    model = DocumentoRequisitoInscricao
    extra = 0
    readonly_fields = ['servico']



class InscricaoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'edital']
    list_filter = ['status']
    filter_horizontal = ['servicos']
    readonly_fields = ['servicos']
    inlines = [DocumentoRequisitoInscricaoInline]


admin.site.register(Edital, EditalAdmin)
admin.site.register(Inscricao, InscricaoAdmin)
# admin.site.register(PoloAtuacao, PoloAtuacaoAdmin)
# admin.site.register(Contratante, ContratanteAdmin)
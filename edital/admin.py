from django.contrib import admin
from .models import Edital, Documento, Requisito, PoloAtuacao, Contratante

class DocumentoInline(admin.StackedInline):
    model = Documento
    extra = 0

class RequisitoInline(admin.StackedInline):
    model = Requisito
    extra = 0

class editalAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'status', 'data_publicacao', 'inicio_inscricao', 'fim_inscricao']
    list_filter = ['status']
    inlines = [DocumentoInline, RequisitoInline]

class PoloAtuacaoAdmin(admin.ModelAdmin):
    list_display = ['nome']

class ContratanteAdmin(admin.ModelAdmin):
    list_display = ['nome']

admin.site.register(Edital, editalAdmin)
admin.site.register(PoloAtuacao, PoloAtuacaoAdmin)
admin.site.register(Contratante, ContratanteAdmin)
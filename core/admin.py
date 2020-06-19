from django.contrib import admin
from .models import *

class RequisitoInline(admin.StackedInline):
    model = Requisito
    extra = 0


class ServicoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'polo_atuacao']
    inlines = [RequisitoInline]

class DocumentoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['titulo']

class PoloAtuacaoAdmin(admin.ModelAdmin):
    list_display = ['nome']


class ContratanteAdmin(admin.ModelAdmin):
    list_display = ['nome']


admin.site.register(PoloAtuacao, PoloAtuacaoAdmin)
admin.site.register(Contratante, ContratanteAdmin)
admin.site.register(DocumentoUsuario, DocumentoUsuarioAdmin)
admin.site.register(Servico, ServicoAdmin)
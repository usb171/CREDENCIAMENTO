from django.contrib import admin
from .models import Usuario

class usuarioAdmin(admin.ModelAdmin):
    list_display = ['ativo', 'nome', 'cpf', 'ativo']
    search_fields = ['nome', 'cpf']
    list_filter = ['ativo']

admin.site.register(Usuario, usuarioAdmin)

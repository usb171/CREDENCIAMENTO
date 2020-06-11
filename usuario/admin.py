from django.contrib import admin
from .models import Usuario

class usuarioAdmin(admin.ModelAdmin):
    list_display = ['email', 'ativo', 'categoria_pessoa']
    search_fields = ['email', 'categoria_pessoa']
    list_filter = ['ativo', 'categoria_pessoa']

admin.site.register(Usuario, usuarioAdmin)

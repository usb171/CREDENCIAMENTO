from django.contrib import admin
from .models import Edital, Documento


class DocumentoInline(admin.StackedInline):
    model = Documento
    extra = 0


class editalAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'status', 'data_publicacao', 'inicio_inscricao', 'fim_inscricao']
    list_filter = ['status']
    inlines = [DocumentoInline]

admin.site.register(Edital, editalAdmin)
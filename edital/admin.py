from django.contrib import admin

from .models import Edital

class editalAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'status', 'data_publicacao', 'inicio_inscricao', 'fim_inscricao']
    list_filter = ['status']

admin.site.register(Edital, editalAdmin)
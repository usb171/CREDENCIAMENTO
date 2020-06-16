from django.urls import path
from .views import Edital

urlpatterns = [
    path('inscricao', Edital.inscricao, name='inscricao'),
    path('minhasInscricoes', Edital.minhasInscricoes, name='minhasInscricoes'),
]
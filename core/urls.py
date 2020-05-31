from django.urls import path
from .views import Core, CoreAjax

urlpatterns = [
    path('', Core.index, name='index'),
    path('get_edital_ajax', CoreAjax.get_edital, name='get_edital_ajax'),
    path('nova_inscricao_edital_ajax', CoreAjax.nova_inscricao_edital, name='nova_inscricao_edital_ajax'),
]
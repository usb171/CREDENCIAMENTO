from django.urls import path
from .views import Core, CoreAjax

urlpatterns = [
    path('', Core.index, name='index'),
    path('get_edital_ajax', CoreAjax.get_edital_ajax, name='get_edital_ajax'),
]
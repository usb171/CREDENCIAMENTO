from django.shortcuts import render
from .ferramentas.buscas import *
from django.http import JsonResponse

class Core:

    def index(request):
        template_name = "core/index.html"
        context = {
            'rodape': [],
            'editais': [],
        }
        if request.method == 'GET':
            context['editais'] = get_editais()
            return render(request=request, template_name=template_name, context=context)


class CoreAjax:

    def get_edital_ajax(request):
        descricao_html = get_descricao_edital_html(request)
        return JsonResponse({'descricao': descricao_html})
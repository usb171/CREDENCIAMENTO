from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .ferramentas.buscas import *
from core.ferramentas.buscas import *
from .ferramentas.funcoes import *

class Edital:

    @login_required(login_url='index')
    def inscricao(request):
        template_name = "edital/inscricao.html"
        context = {
            'rodape': [],
            'edital': get_edital(request),
            'edital_html': get_descricao_edital_html_2(request),
            'servicos_selecionados': get_ids_servicos_inscricao(request)
        }

        if request.method == 'GET':
            return render(request=request, template_name=template_name, context=context)
        elif request.method == 'POST':
            inscrever(request)
            return render(request=request, template_name=template_name, context=context)


    @login_required(login_url='index')
    def minhasInscricoes(request):
        template_name = "edital/minhasInscricoes.html"
        context = {'usuario': get_usuario(request)}
        if request.method == 'GET':
            return render(request=request, template_name=template_name, context=context)
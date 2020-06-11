from django.shortcuts import render, redirect
from .ferramentas.buscas import *
from .ferramentas.funcoes import *
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout

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

    def login(request):
        if request.method == 'POST':
            context = criarEditarLogin(request)
            return JsonResponse(context)

    def logout(request):
        auth_logout(request)
        return redirect('index')

    def novoUsuario(request):
        if request.method == 'POST':
            context = criarEditarLogin(request)
            return JsonResponse(context)

    def editarMeusDados(request):
        if request.method == 'POST':
            context = criarEditarLogin(request)
            return JsonResponse(context)


class CoreAjax:

    def buscarEmail(request):
        email = get_email(request)
        return JsonResponse(email)

    def buscarCpf(request):
        cpf = get_cpf(request)
        return JsonResponse(cpf)

    def buscarCnpj(request):
        cnpj = get_cnpj(request)
        return JsonResponse(cnpj)

    def get_editais_filtros(request):
        editais = get_editais_html(request)
        return JsonResponse({'editais': editais})

    def get_edital_descricao(request):
        descricao_html = get_descricao_edital_html(request)
        return JsonResponse({'descricao': descricao_html})

    def validar_login_usuario(request):
        flag_login = request.user.is_authenticated
        return JsonResponse({'login_flag': flag_login})
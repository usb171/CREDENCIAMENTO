from edital.models import Edital, Documento, Requisito
from usuario.models import Usuario
from django.db.models import Q
from .funcoes import *


def get_usuario(request):
    try:
        user = request.user
        if user is not None:
            return  Usuario.objects.get(user=user)
        else:
            return None
    except Exception as e:
        print(e)
        return None


def get_email(request):
    email = request.GET.get('email', None)
    if email:
        email = list(map(lambda x: x['email'], Usuario.objects.filter(email__contains=email).values('email')))
        if email:
            return dict(flag=True, email=email)
        else:
            return dict(flag=False, email=email)
    else:
        return dict(flag=False)


def get_cpf(request):
    cpf = request.GET.get('cpf', None)
    if cpf:
        cpf = list(map(lambda x: x['cpf'], Usuario.objects.filter(cpf__contains=cpf).values('cpf')))
        if cpf:
            return dict(flag=True, cpf=cpf)
        else:
            return dict(flag=False, cpf=cpf)
    else:
        return dict(flag=False)


def get_cnpj(request):
    cnpj = request.GET.get('cnpj', None)
    if cnpj:
        cnpj = list(map(lambda x: x['cnpj'], Usuario.objects.filter(cnpj__contains=cnpj).values('cnpj')))
        if cnpj:
            return dict(flag=True, cnpj=cnpj)
        else:
            return dict(flag=False, cnpj=cnpj)
    else:
        return dict(flag=False)


def get_rodape():
    rodape = []
    return rodape


def filtros_buscas(request):

    ano = request.GET.get('ano')
    categoria = request.GET.get('categoria')
    editais = Edital.objects

    if ano != "%":
        '''
            Se for um ano específico
        '''
        if categoria == "2":
            '''
                Se for uma pessoa física/jurídica
            '''
            editais = editais.order_by('-data_publicacao').filter(ano_publicacao=ano,
                                                                  status__in=['1', '2', '3'])
        else:
            editais = editais.order_by('-data_publicacao').filter(ano_publicacao=ano,
                                                                  status__in=['1', '2', '3'],
                                                                  categoria=categoria)
    else:
        '''
            Se for todos os anos
        '''
        if categoria == "2":
            '''
                Se for uma pessoa física/jurídica
            '''
            editais = editais.order_by('-data_publicacao').filter(status__in=['1', '2', '3'])
        else:
            editais = editais.order_by('-data_publicacao').filter(status__in=['1', '2', '3'],
                                                                  categoria=categoria)

    return editais


def get_editais():
    return Edital.objects.order_by("-data_publicacao").filter(status__in=['1', '2', '3'])


def get_editais_html(request):

    editais = filtros_buscas(request)

    editais_html = ''
    card_html = '<div class="edital content-wrap" onclick="abrirDescricaoEdital({id})">' \
                    '<div class="container clearfix">' \
                        '<div class="card">' \
                            '<div class="card-header">' \
                                'Edital N° {codigo}' \
                            '</div>' \
                            '<div class="card-body">' \
                            '<h5 class="card-title">' \
                                '<span>Categoria:</span> {categoria} <br>' \
                                '<span>Andamento:</span> {status} <br>' \
                                '<span>Título:</span> {titulo} <br>' \
                            '</h5>' \
                            '</div>' \
                        '</div>' \
                    '</div>' \
                '</div>'

    for edital in editais:
        editais_html = editais_html + card_html.format(id=edital.id,
                                                       codigo=edital.codigo,
                                                       categoria=edital.get_categoria(),
                                                       status=edital.get_status(),
                                                       titulo=edital.titulo)

    return editais_html


def get_descricao_edital_html(request):
    try:
        edital = Edital.objects.get(id=request.GET.get('id'))

        html = '<h5>' \
               '<div class="l-1"><span>Edital Nº: </span>{codigo}</div>' \
               '<div class="l-2"><span>Categoria: </span>{categoria}</div>' \
               '<div class="l-1"><span>Andamento: </span>{andamento}</div>' \
               '<div class="l-2"><span>Data da Publicação: </span>{data_publicacao}</div>' \
               '<div class="l-1"><span>Período de Inscrição: </span>{inicio_inscricao} &nbsp; ao &nbsp; {fim_inscricao}</div>' \
               '<div class="l-2"><span>Título: </span>{titulo}</div>' \
               '<div class="l-1"><span>Descrição: </span>{descricao}</div>' \
               '<div class="l-2">{documentos}</div>' \
               '</h5>' \
               '{button}'
        button_html = '<div class="row">' \
                      '<div class="col-md-12" style="text-align: end;">' \
                      '<a href="#" onClick="validar_login_usuario_redirecionar_inscricao({id})" class="button button-border button-rounded button-fill fill-from-right button-blue">' \
                      '<span>Inscreva-se</span>' \
                      '</a>' \
                      '</div>' \
                      '</div>'

        documentos_html = ""
        for documento in Documento.objects.filter(edital=edital):
            documentos_html = documentos_html + "<a href='{doc}' target='_blank'><img src='static/assets/site1/images/icons/documento.png' style='height: 25px;'></img><i style='text-decoration: underline !important;'>{titulo}</i></a><br>".format(
                doc=documento.get_absolute_url(),
                titulo=documento.titulo)


        return html.format(codigo=edital.codigo,
                           categoria=edital.get_categoria(),
                           andamento=edital.get_status(),
                           data_publicacao=dataHora_BR(edital.data_publicacao),
                           inicio_inscricao=dataHora_BR(edital.inicio_inscricao),
                           fim_inscricao=dataHora_BR(edital.fim_inscricao),
                           titulo=edital.titulo,
                           descricao=edital.descricao,
                           documentos=documentos_html,
                           button=button_html.format(id=edital.id))
    except Exception as e:
        print(e)
        return "<h1>Erro ao carregar edital !!</h1>"


def get_descricao_edital_html_2(request):
    try:
        edital = Edital.objects.get(id=request.GET.get('id'))

        html = '<h4>' \
               '<div class="l-1"><span>Edital Nº: </span>{codigo}</div>' \
               '<div class="l-2"><span>Categoria: </span>{categoria}</div>' \
               '<div class="l-1"><span>Andamento: </span>{andamento}</div>' \
               '<div class="l-2"><span>Data da Publicação: </span>{data_publicacao}</div>' \
               '<div class="l-1"><span>Período de Inscrição: </span>{inicio_inscricao} &nbsp; ao &nbsp; {fim_inscricao}</div>' \
               '<div class="l-2"><span>Título: </span>{titulo}</div>' \
               '<div class="l-1"><span>Descrição: </span>{descricao}</div>' \
               '<div class="l-2">{documentos}</div>' \
               '</h4>' \
               '<h4> Faça o upload dos arquivos requisitados no Edital </h4>' \
               '{campos_arquivos}'\
               '{button}'

        button_html = '<div class="row">' \
                      '<div class="col-md-12 mb-5" style="text-align: end;">' \
                      '<a href="#" onClick="realizar_inscricao({id})" class="button button-border button-rounded button-fill fill-from-right button-blue">' \
                      '<span>Finalizar Inscrição</span>' \
                      '</a>' \
                      '</div>' \
                      '</div>'

        campos_html = ""
        for campo_documento in Requisito.objects.filter(edital=edital):
            campos_html = campos_html + "<div class='form-group l-1'>" \
                                        "<label for='{id}'>{titulo}</label>" \
                                        "<input type='file' class='form-control-file' id='{id}'>" \
                                        "</div>".format(id="campo_documento" + str(campo_documento.id), titulo=campo_documento.titulo)


        documentos_html = ""
        for documento in Documento.objects.filter(edital=edital):
            documentos_html = documentos_html + "<a href='{doc}' target='_blank'><img src='../static/assets/site1/images/icons/documento.png' style='height: 25px;'></img><i style='text-decoration: underline !important;'>{titulo}</i></a><br>".format(
                doc=documento.get_absolute_url(),
                titulo=documento.titulo)


        return html.format(codigo=edital.codigo,
                           categoria=edital.get_categoria(),
                           andamento=edital.get_status(),
                           data_publicacao=dataHora_BR(edital.data_publicacao),
                           inicio_inscricao=dataHora_BR(edital.inicio_inscricao),
                           fim_inscricao=dataHora_BR(edital.fim_inscricao),
                           titulo=edital.titulo,
                           descricao=edital.descricao,
                           documentos=documentos_html,
                           button=button_html.format(id=edital.id),
                           campos_arquivos=campos_html
                           )

    except Exception as e:
        print(e)
        return "<h1>Erro ao carregar edital !!</h1>"
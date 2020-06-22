from django.middleware.csrf import get_token
from edital.models import Edital, Inscricao, DocumentoRequisitoInscricao, DocumentoUsuarioInscricao
from core.models import Documento, Requisito, PoloAtuacao, Contratante, Servico
from usuario.models import Usuario
from .funcoes import *
import re


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


def get_inscricao(request):
    try:
        id = request.GET.get('id')
        if id is None: id = request.GET.get('id_edital')
        id = re.sub("\D", "", id)
        return Inscricao.objects.get(usuario=get_usuario(request), edital=Edital.objects.get(id=id))
    except Exception as e:
        print(e)
        return None


def get_ids_servicos_inscricao(request):
    try:
        return list(map(lambda x: x.id, get_inscricao(request).servicos.all()))
    except Exception as e:
        print(e)
        return None


def get_field_ids_inscricao_servicos(request):
    return '<input id="id_servicos_select2_val" value = "{}" hidden>'.format(get_ids_servicos_inscricao(request))


def get_editais():
    return Edital.objects.order_by("-data_publicacao").filter(status__in=['1', '2', '3'])


def get_editais_minhas_inscricoes(request):
    return list(map(lambda inscricao: inscricao.edital, Inscricao.objects.filter(usuario=get_usuario(request))))


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


def get_documentos_usuario_html(request):

    edital = Edital.objects.get(id=request.GET.get('id'))
    documentos = edital.documentos_usuario.all()
    inscricao = get_inscricao(request)

    blocos_html = ''

    bloco_html = '<div class="card mt-4">' \
                    '<h4 class="card-header">Documentos do Usuário </h4>' \
                    '<div class="card-body">' \
                        '{bloco}' \
                    '</div>' \
                 '</div>'


    documentos_usuario_html = '<div class="card mt-4">' \
                                  '<h4 class="card-header"> {nome_arquivo} </h4>' \
                                  '<div class="card-body">' \
                                      '<div style="display: {flag_show_retorno_avaliacao}">' \
                                          '<div class="l-1"><span>Status do Documento: </span>{status_documento}</div>' \
                                          '<div class="l-2"><span>Documento Atual: </span>' \
                                              '<a href="{link_arquivo}" target="_blank">' \
                                                    '<img src="../static/assets/site1/images/icons/documento.png" style="height: 25px;">' \
                                                    '<i style="text-decoration: underline !important;">Documento</i>' \
                                              '</a>' \
                                          '</div>' \
                                          '<div class="l-1"><span>Atualizado em: </span>{atualizado_em}</div>' \
                                          '<div class="l-2"><span>Observação do Avaliador: </span>{observacao_avaliador}</div>' \
                                      '</div>' \
                                      '<div style="display: {flag_show_upload_arquivo}">' \
                                            '<div class="input-group l-1">' \
                                                '<input type="file" name="files_usuario[{id}]" id="file_usuario_{id}" onchange="{evento_set_nome_arquivo}" accept="application/pdf, image/jpeg, image/png, image/jpg" class="form-control" style="display: none">' \
                                                '<input type="text" id="id_text_file_usuario_{id}" class="form-control" value="{nome_documento}" readonly="" required>' \
                                                '<span class="input-group-btn">' \
                                                    '<a onclick="{evento_abrir_arquivo}" class="button button-3d button-blue "style="margin-top: -1px; color: aliceblue;">Procurar Arquivo</a>' \
                                                '</span>' \
                                            '</div>' \
                                            '<div class="l-2" style="display: {flag_show_cancelar_documento}">' \
                                                '<a onclick="cancelar_documento_usuario({id_usuario});" style="cursor: pointer; color: red; font-size: smaller; text-decoration: underline !important;">' \
                                                    'Cancelar Documento' \
                                                '</a>' \
                                           '</div>' \
                                      '</div>' \
                                  '</div>' \
                              '</div>' \

    for documento in documentos:
        documento_usuario_inscricao = DocumentoUsuarioInscricao.objects.filter(inscricao=inscricao, documento_usuario=documento).first()
        id_usuario = ''
        link_arquivo = ''
        atualizado_em = ''
        nome_documento = ''
        status_documento = ''
        observacao_avaliador = ''
        flag_show_upload_arquivo = ''
        flag_show_cancelar_documento = 'none'
        flag_show_retorno_avaliacao = 'none'
        if documento_usuario_inscricao is not None:
            id_usuario = documento_usuario_inscricao.id
            flag_show_cancelar_documento = 'none' if documento_usuario_inscricao.status == '1' else ''
            link_arquivo = documento_usuario_inscricao.documento.url
            atualizado_em = dataHora_BR(documento_usuario_inscricao.update_at)
            nome_documento = documento_usuario_inscricao.get_nome_documento()
            status_documento = documento_usuario_inscricao.get_status()
            observacao_avaliador = documento_usuario_inscricao.observacao
            flag_show_upload_arquivo = 'none' if documento_usuario_inscricao.status == '1' else ''
            flag_show_retorno_avaliacao = ''

        blocos_html = blocos_html + documentos_usuario_html.format(id=documento.id,
                                                                   id_usuario=id_usuario,
                                                                   link_arquivo=link_arquivo,
                                                                   atualizado_em=atualizado_em,
                                                                   nome_documento=nome_documento,
                                                                   nome_arquivo=documento.titulo,
                                                                   status_documento=status_documento,
                                                                   observacao_avaliador=observacao_avaliador,
                                                                   flag_show_upload_arquivo=flag_show_upload_arquivo,
                                                                   flag_show_retorno_avaliacao=flag_show_retorno_avaliacao,
                                                                   flag_show_cancelar_documento=flag_show_cancelar_documento,
                                                                   evento_set_nome_arquivo="$('#id_text_file_usuario_{id}').val($('#file_usuario_{id}')[0].files[0].name);".format(id=documento.id),
                                                                   evento_abrir_arquivo="$('#file_usuario_{id}').trigger('click');".format(id=documento.id),
                                                                   )
    # return ''
    return bloco_html.format(bloco=blocos_html)


def get_servicos_edital_html(request, edital):
    try:
        servicos = edital.servicos.all()
        if servicos.exists():
            select2_html =  '<div class="card mt-4">' \
                                '<h4 class="card-header"> Selecione os serviços para inscrição </h4>' \
                                '<div class="card-body">' \
                                    '<select id="id_servicos_select2" class="select2 select2-lg" multiple="" required>' \
                                    '{options}' \
                                    '</select>' \
                                '</div>' \
                            '</div>' \
                            '<div id="id_blocos_servicos"></div>'

            options = ""
            for servico in servicos:
                options = options + '<option value="{id}">{titulo}</option>'.format(id=servico.id, titulo=servico)

            return select2_html.format(options=options)
        else:
            return ''
    except Exception as e:
        return '<h4 style="color:red"> Erro ao gerar serviços do Edital </4>'


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

        html = '<div class="edital-descricao">'\
                   '<h5>' \
                   '<div class="l-1"><span>Edital Nº: </span>{codigo}</div>' \
                   '<div class="l-2"><span>Categoria: </span>{categoria}</div>' \
                   '<div class="l-1"><span>Andamento: </span>{andamento}</div>' \
                   '<div class="l-2"><span>Data da Publicação: </span>{data_publicacao}</div>' \
                   '<div class="l-1"><span>Período de Inscrição: </span>{inicio_inscricao} &nbsp; ao &nbsp; {fim_inscricao}</div>' \
                   '<div class="l-2"><span>Título: </span>{titulo}</div>' \
                   '<div class="l-1"><span>Descrição: </span>{descricao}</div>' \
                   '<div class="l-2">{documentos}</div>' \
                   '<form action="" method="post" enctype="multipart/form-data" id="form_inscricao">' \
                        '<input type="hidden" name="csrfmiddlewaretoken" value="{CSRF}">' \
                        '{servicos}' \
                        '{documentos_usuario}' \
                        '{button}' \
                   '</form>' \
                   '{field_ids_inscricao_servicos}' \
                   '</h5>' \
                '</div>'


        button_html = '<div class="row">' \
                      '<div class="col-md-12 mt-4" style="text-align: end;">' \
                      '<button href="#" class="button button-border button-rounded button-fill fill-from-right button-blue">' \
                      '<span>Finalizar Inscrição</span>' \
                      '</button>' \
                      '</div>' \
                      '</div>'

        servicos = get_servicos_edital_html(request, edital)

        documentos_html = ""
        for documento in Documento.objects.filter(edital=edital):
            documentos_html = documentos_html + "<a href='{doc}' target='_blank'><img src='../static/assets/site1/images/icons/documento.png' style='height: 25px;'></img><i style='text-decoration: underline !important;'>{titulo}</i></a><br>".format(
                doc=documento.get_absolute_url(),
                titulo=documento.titulo)

        return html.format(codigo=edital.codigo,
                           servicos=servicos,
                           titulo=edital.titulo,
                           CSRF=get_token(request),
                           documentos=documentos_html,
                           descricao=edital.descricao,
                           andamento=edital.get_status(),
                           categoria=edital.get_categoria(),
                           button=button_html.format(id=edital.id),
                           fim_inscricao=dataHora_BR(edital.fim_inscricao),
                           data_publicacao=dataHora_BR(edital.data_publicacao),
                           inicio_inscricao=dataHora_BR(edital.inicio_inscricao),
                           documentos_usuario=get_documentos_usuario_html(request),
                           field_ids_inscricao_servicos=get_field_ids_inscricao_servicos(request),
                           )

    except Exception as e:
        print(e)
        return "<h1>Erro ao carregar edital !!</h1>"


def get_blocos_campos_arquivos_servicos(request):
    ids_selecionados = request.GET.get('ids_selected').split(',')
    id_edital = request.GET.get('id_edital')
    inscricao = get_inscricao(request)

    blocos_html = ''

    bloco_html = '<div class="card mt-4">' \
                    '<h4 class="card-header"> {header} </h4>' \
                    '<div class="card-body"> {body} </div>' \
                 '</div>'

    requisito_html = '<div class="card mt-2">' \
                        '<h4 class="card-header"> {header} </h4>' \
                        '<div class="card-body"> {body} </div>' \
                     '</div>'


    body_bloco_retorno_html = '<div class="l-1"><span>Status do Documento: </span>{status_documento}</div>' \
                               '<div class="l-2"><span>Documento Atual: </span>' \
                                    '<a href="{link_arquivo}" target="_blank">' \
                                        '<img src="../static/assets/site1/images/icons/documento.png" style="height: 25px;">' \
                                        '<i style="text-decoration: underline !important;">Documento</i>' \
                                    '</a>' \
                               '</div>' \
                               '<div class="l-1"><span>Atualizado em: </span>{atualizado_em}</div>' \
                               '<div class="l-2"><span>Observação do Avaliador: </span>{observacao_avaliador}</div>' \


    button_cancelar_documento = '<div class="l-2" style="display: {flag_show_button_cancelar_documento}">' \
                                    '<a onclick="cancelar_documento_requisito({id_documento});" style="cursor: pointer; color: red; font-size: smaller; text-decoration: underline !important;">' \
                                        'Cancelar Documento' \
                                    '</a>' \
                               '</div>' \


    body_bloco_html =  '{body_bloco_retorno_html}'\
                       '<div class="input-group l-1" style="display: {flag_show_upload_arquivo}">' \
                            '<input type="file" name="files[{id}]" id="file_{id}" onchange="{evento_set_nome_arquivo}" accept="application/pdf, image/jpeg, image/png, image/jpg" class="form-control" style="display: none">'\
                            '<input type="text" id="id_text_file_{id}" class="form-control" value="{nome_arquivo}" readonly="">'\
                            '<span class="input-group-btn">'\
                                '<a onclick="{evento_abrir_arquivo}" class="button button-3d button-blue "style="margin-top: -1px; color: aliceblue;">Procurar Arquivo</a>' \
                            '</span>'\
                       '</div>' \
                       '{button_cancelar_documento}'\


    if ids_selecionados[0] is not '' and id_edital is not '':
        for servico in  Servico.objects.filter(id__in=ids_selecionados):
            body_servico = ''
            for requisito in Requisito.objects.filter(servico=servico):
                nome_arquivo = ''
                link_arquivo = ''
                status_documento = ''
                atualizado_em = ''
                body_bloco_retorno_html_aux = ''
                observacao_avaliador = ''
                button_cancelar_documento_aux = ''
                flag_show_upload_arquivo = ''
                flag_show_button_cancelar_documento = ''
                if inscricao is not None and requisito is not None:
                    documento = DocumentoRequisitoInscricao.objects.filter(requisito=requisito, inscricao=inscricao)
                    if documento:
                        nome_arquivo = documento.first().get_nome_documento()
                        link_arquivo = documento.first().documento.url
                        status_documento = documento.first().get_status()
                        atualizado_em = dataHora_BR(documento.first().update_at)
                        observacao_avaliador = documento.first().observacao
                        flag_show_upload_arquivo = 'none' if documento.first().status is '1' else ''
                        flag_show_button_cancelar_documento = 'none' if documento.first().status is '1' else ''
                        button_cancelar_documento_aux = button_cancelar_documento.format(id_documento=documento.first().id,
                                                                                         flag_show_button_cancelar_documento=flag_show_button_cancelar_documento)
                        body_bloco_retorno_html_aux = body_bloco_retorno_html.format(status_documento=status_documento,
                                                                                     link_arquivo=link_arquivo,
                                                                                     observacao_avaliador=observacao_avaliador,
                                                                                     atualizado_em=atualizado_em
                                                                                 )
                body_bloco_requisito = body_bloco_html.format(id=requisito.id,
                                                              nome_arquivo=nome_arquivo,
                                                              body_bloco_retorno_html=body_bloco_retorno_html_aux,
                                                              evento_set_nome_arquivo="$('#id_text_file_{id}').val($('#file_{id}')[0].files[0].name);".format(id=requisito.id),
                                                              evento_abrir_arquivo="$('#file_{id}').trigger('click');".format(id=requisito.id),
                                                              button_cancelar_documento=button_cancelar_documento_aux,
                                                              flag_show_upload_arquivo=flag_show_upload_arquivo
                                                              )

                body_servico = body_servico + requisito_html.format(header=requisito.titulo, body=body_bloco_requisito)

            blocos_html = blocos_html + bloco_html.format(header=servico, body=body_servico)

    return blocos_html
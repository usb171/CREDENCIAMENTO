from edital.models import Edital, Documento
from .funcoes import *

def get_rodape():
    rodape = []
    return rodape


def get_editais():
    return Edital.objects.order_by("data_publicacao").filter(status__in=['1', '2', '3'])


def get_descricao_edital_html(request):
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
               '{button}'
        button_html = '<div class="row">' \
                      '<div class="col-md-12" style="text-align: end;">' \
                      '<a href="#" onClick="novaInscricao({id})" class="button button-border button-rounded button-fill fill-from-right button-blue">' \
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
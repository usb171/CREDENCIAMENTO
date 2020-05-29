from edital.models import Edital


def get_rodape():
    rodape = []
    return rodape


def get_editais():
    return Edital.objects.order_by("data_publicacao").filter(status__in=['1', '2', '3'])


def get_descricao_edital_html(request):
    return '<h1>Descrição</h1>'
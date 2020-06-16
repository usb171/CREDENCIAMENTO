import re
from core.models import Documento, Requisito, PoloAtuacao, Contratante, Servico
from edital.models import Edital, Inscricao, DocumentoRequisitoInscricao
from core.ferramentas.buscas import *

def inscrever(request):

    usuario = get_usuario(request)
    edital = Edital.objects.get(id=request.GET.get('id'))

    for name_field, file in request.FILES.items():
        id_requisito = re.sub("\D", "", name_field)
        requisito = Requisito.objects.get(id=id_requisito)
        servico = requisito.servico
        inscricao, criado_inscricao = Inscricao.objects.get_or_create(usuario=usuario, edital=edital)
        inscricao.servicos.add(servico)

        documentoRequisitoInscricao, criado_documentoRequisitoInscricao = DocumentoRequisitoInscricao.objects.get_or_create(inscricao=inscricao, servico=servico, requisito=requisito)
        if criado_documentoRequisitoInscricao:
            documentoRequisitoInscricao.requisito = requisito

        documentoRequisitoInscricao.documento = file
        if documentoRequisitoInscricao.status is not '1': documentoRequisitoInscricao.status = '0'
        documentoRequisitoInscricao.save()
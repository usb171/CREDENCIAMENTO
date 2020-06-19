import re
from core.models import Documento, Requisito, PoloAtuacao, Contratante, Servico, DocumentoUsuario
from edital.models import Edital, Inscricao, DocumentoRequisitoInscricao, DocumentoUsuarioInscricao
from core.ferramentas.buscas import *

def inscrever(request):

    usuario = get_usuario(request)
    edital = Edital.objects.get(id=request.GET.get('id'))

    for name_field, file in request.FILES.items():

        id_requisito_ou_documento = re.sub("\D", "", name_field)

        if name_field.find('usuario') is -1:
            print("Documento do Serviço")
            requisito = Requisito.objects.get(id=id_requisito_ou_documento)
            servico = requisito.servico
            inscricao, criado_inscricao = Inscricao.objects.get_or_create(usuario=usuario, edital=edital)
            inscricao.servicos.add(servico)

            documentoRequisitoInscricao, criado_documentoRequisitoInscricao = DocumentoRequisitoInscricao.objects.get_or_create(
                inscricao=inscricao, servico=servico, requisito=requisito)

            if criado_documentoRequisitoInscricao:
                documentoRequisitoInscricao.requisito = requisito

            documentoRequisitoInscricao.documento = file
            if documentoRequisitoInscricao.status is not '1': documentoRequisitoInscricao.status = '0'
            documentoRequisitoInscricao.save()
        else:
            print("Documento do usuario")
            documento_usuario = DocumentoUsuario.objects.get(id=id_requisito_ou_documento)
            inscricao, criado_inscricao = Inscricao.objects.get_or_create(usuario=usuario, edital=edital)
            documentoUsuarioInscricao, criado_documentoUsuarioInscricao = DocumentoUsuarioInscricao.objects.get_or_create(
                inscricao=inscricao, documento_usuario=documento_usuario)

            if criado_documentoUsuarioInscricao:
                documentoUsuarioInscricao.documento_usuario = documento_usuario

            documentoUsuarioInscricao.documento = file
            if documentoUsuarioInscricao.status is not '1': documentoUsuarioInscricao.status = '0'
            documentoUsuarioInscricao.save()



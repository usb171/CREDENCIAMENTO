import string
import random
from .buscas import *
from .sessao import *
from django.contrib.auth.models import User
from usuario.models import Usuario
from django.contrib.auth import login as loginAuth
from edital.models import DocumentoRequisitoInscricao, DocumentoUsuarioInscricao
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def gerar_senha(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def enviar_email(subject, from_email, to, template, values):
    html_message = render_to_string(template, values)
    plain_message = strip_tags(html_message)
    return mail.send_mail(subject, plain_message, from_email, [to], html_message)


def dataHora_BR(dataTime):
    return dataTime.strftime("%d/%m/%Y %H:%M")


def cancelar_documento_requisito(request):
    documento = DocumentoRequisitoInscricao.objects.get(id=request.GET.get('id'))
    if documento is not None:
        documento.delete()
        return True
    else:
        return False


def cancelar_documento_usuario(request):
    documento = DocumentoUsuarioInscricao.objects.get(id=request.GET.get('id'))
    if documento is not None:
        documento.delete()
        return True
    else:
        return False


def login(formulario, request):
    return Sessao.login(email=formulario['email'], senha=formulario['senha'], request=request)


def criar(formulario, request):
    try:
        erros = {}
        if formulario['email'] != formulario['cemail']:
            erros['cemail'] = ['Email não corresponde']
        if erros:
            return {'status': False, 'erros': erros}

        formulario['senha'] = gerar_senha()
        formulario['user'] = User.objects.create_user(username=formulario['email'], email=formulario['email'],
                                                      password=formulario['senha'], is_active=True)

        enviar_email(subject='Credenciamento FIEPI/SESI/SENAI',
                     from_email='credenciamento@fiepi.com',
                     template='usuario/email/descricao_acesso_portal.html',
                     to=formulario['email'],
                     values={'email': formulario['email'], 'senha': formulario['senha']}
                     )

        del formulario['cemail']
        del formulario['senha']

        formulario['ativo'] = True
        usuario = Usuario.objects.create(**formulario)

        if formulario['user'] is not None:
            loginAuth(request, formulario['user'])

        else:
            return {'status': False, 'msg': ['Erro ao Logar usuário']}

        return {'status': True, 'usuario': {'id': usuario.id, 'email': usuario.email},
                'msg': 'Usuário cadastrado com sucesso'}
    except Exception as e:
        print(e)
        if 'user' in formulario: formulario['user'].delete()
        return {'status': False, 'msg': ['Erro ao cadastrar usuário']}


def editar(formulario, request):
    try:
        # erros = {}
        # if formulario['email'] != formulario['cemail']:
        #     erros['cemail'] = ['Email não corresponde']
        # if erros:
        #     return {'status': False, 'erros': erros}
        categoria_pessoa = formulario['categoria_pessoa']
        user = User.objects.get(id=request.user.id)
        usuario = Usuario.objects.get(user=user)

        if categoria_pessoa is not "" and categoria_pessoa == "0":
            usuario.nome = formulario['nome']
        elif categoria_pessoa is not "" and categoria_pessoa == "1":
            usuario.razao_social = formulario['razao_social']
            usuario.nome_fantasia = formulario['nome_fantasia']
            usuario.cnpj_nome = formulario['cnpj_nome']

        usuario.sexo = formulario['sexo']
        usuario.telefone = formulario['telefone']
        usuario.estado = formulario['estado']
        usuario.cidade = formulario['cidade']
        usuario.endereco = formulario['endereco']
        usuario.numero = formulario['numero']
        usuario.bairro = formulario['bairro']
        usuario.cep = formulario['cep']
        usuario.save()
        return {'status': True, 'msg': 'Dados editados sucesso'}

    except Exception as e:
        print(e)
        return {'status': False, 'msg': ['Erro ao editar dados']}


def criarEditarLogin(request, fazerInscricao=False):
    formulario = request.POST.copy()
    comando = formulario['comando']
    del formulario['comando']
    del formulario['csrfmiddlewaretoken']

    formulario = {k: str(v[0]) for k, v in dict(formulario).items() if isinstance(v, (list,))}

    if comando == '#criar#':
        return criar(formulario, request)
    elif comando == '#editar#':
        return editar(formulario, request)
    elif comando == '#login#':
        return login(formulario, request)
    elif comando == '#alterarSenha#':
        pass
        # return alterarSenha(request)
    else:
        return {'status': False, 'msg': ['Não foi possível executar o comando: ' + str(comando)]}
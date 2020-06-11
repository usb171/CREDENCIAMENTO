from usuario.models import Usuario
from django.contrib.auth import authenticate, update_session_auth_hash, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import PasswordChangeForm

class Sessao():
    """
    *  Método Login
    *  Recebe email e senha, autentica e loga o usuário a uma nova sessão
    """
    def login(email, senha, request):
        context = {
            'logado': True,
            'msg': '',
            'email': email,
            'senha': senha,
        }

        '''Busque o usuário que contenha o email em questão'''
        try:
            usuario = Usuario.objects.get(email=email)
            ativo = usuario.ativo
            if ativo:
                user = usuario.user
                '''Faça a autenticação do usuário'''
                user = authenticate(request, username=user.username, password=senha)  # Faz a autenticação do usuário
                '''Se o usuário existir e for autenticado'''
                if user is not None:
                    auth_login(request, user)
                else:
                    context['msg'] = 'Não foi possível autenticar o usuário'
                    context['logado'] = False
            else:
                context['msg'] = 'Usuário desativado'
                context['logado'] = False
        except Exception as e:
            print(e)
            context['msg'] = 'E-mail não encontrado'
            context['logado'] = False

        return context

    def logout(request):
        auth_logout(request)

    def alterar_senha(request):
        context = {
            'alterado': True,
            'msg': '',
            'erros': None,
        }

        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            context['msg'] = "Atualizado com sucesso"
            return context
        else:
            context['alterado'] = False
            context['erros'] = form.errors
            context['msg'] = "Erro nos seguintes campos"
            return context
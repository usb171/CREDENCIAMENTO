from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Usuario
from django.shortcuts import render


def enviarAtivador(user, request, form):
    current_site = get_current_site(request)
    conta = Usuario.objects.get(user=user)
    mail_subject = 'Ative sua conta.'
    message = render_to_string('usuario/email/modelo_ativar_email.html', {
        'user': user,
        'conta': conta,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        'token': account_activation_token.make_token(user),
    })

    to_email = form.cleaned_data.get('email')
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()

def ativarAcesso(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        conta = Usuario.objects.get(user=user)
        conta.ativo = True
        conta.save()
        login(request, user)
        return render(request, 'usuario/email/acesso_confirmado.html')
    else:
        return render(request, 'usuario/email/acesso_negado.html')


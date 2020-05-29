from django.db import models
from core.ferramentas.enumerate import ESTADOS
from django.contrib.auth.models import User

class Usuario(models.Model):
    """
        *   Classe Usuario
        *   Classe que extende a classe padrão `user` com objetivo de acrescentar mais atributos
    """
    ativo = models.BooleanField(verbose_name='Ativar essa Conta ?', default=False)
    user = models.OneToOneField(User, verbose_name='Usuário de acesso', on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=150, null=True, verbose_name='* Nome')
    cpf = models.CharField(max_length=50, unique=True, null=True, verbose_name='* CPF', blank=True)
    razao_social = models.CharField(max_length=150, null=True, unique=True, verbose_name='* Razão Social', blank=True)
    nome_fantasia = models.CharField(max_length=150, null=True, verbose_name='* Nome Fantasia', blank=True)
    cnpj = models.CharField(max_length=50, unique=True, null=True, verbose_name='* CNPJ', blank=True)
    cnpj_cpf = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name='* Cpf do Responsável')
    cnpj_nome = models.CharField(max_length=150, verbose_name='* Nome do Responsável', null=True, blank=True)
    sexo = models.CharField(max_length=1, null=True, blank=True)
    telefone = models.CharField(max_length=20, verbose_name='* Telefone')
    endereco = models.CharField(max_length=100, verbose_name='* Endereço')
    numero = models.CharField(max_length=10, verbose_name='* Número')
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50, verbose_name='* Bairro')
    cidade = models.CharField(max_length=50, verbose_name='* Cidade')
    cep = models.CharField(max_length=20, verbose_name="* Cep")
    estado = models.CharField(max_length=2, choices=ESTADOS, verbose_name='* Estado')

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome
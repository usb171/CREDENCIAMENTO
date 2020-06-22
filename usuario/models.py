from django.db import models
from core.ferramentas.enumerate import ESTADOS, SEXO, CATEGORIA_PESSOA
from django.contrib.auth.models import User

class Usuario(models.Model):
    """
        *   Classe Usuario
        *   Classe que extende a classe padrão `user` com objetivo de acrescentar mais atributos
    """
    categoria_pessoa = models.CharField(max_length=1, choices=CATEGORIA_PESSOA, blank=False, null=True)
    ativo = models.BooleanField(verbose_name='Ativar essa Conta ?', default=False)
    user = models.OneToOneField(User, verbose_name='Usuário de acesso', on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=150, verbose_name='Nome', null=True, blank=True)
    email = models.CharField(max_length=150, verbose_name='* E-mail', null=True)
    cpf = models.CharField(max_length=50, verbose_name='CPF', blank=True, null=True)
    razao_social = models.CharField(max_length=150, verbose_name='Razão Social', blank=True, null=True)
    nome_fantasia = models.CharField(max_length=150, verbose_name='Nome Fantasia', blank=True, null=True)
    cnpj = models.CharField(max_length=50, verbose_name='CNPJ', blank=True, null=True)
    cnpj_cpf = models.CharField(max_length=50, verbose_name='Cpf do Responsável', null=True, blank=True)
    cnpj_nome = models.CharField(max_length=150, verbose_name='Nome do Responsável', null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO, default='0', blank=True, null=True)
    telefone = models.CharField(max_length=20, verbose_name='Telefone', null=True, blank=True, default='')
    endereco = models.CharField(max_length=100, verbose_name='Endereço', null=True, blank=True, default='')
    numero = models.CharField(max_length=10, verbose_name='Número', default="S/N", null=True, blank=True)
    complemento = models.CharField(max_length=50, null=True, blank=True, default='')
    bairro = models.CharField(max_length=50, verbose_name='Bairro', null=True, blank=True, default='')
    cidade = models.CharField(max_length=50, verbose_name='Cidade', null=True, blank=True, default='')
    cep = models.CharField(max_length=20, verbose_name="Cep", null=True, blank=True, default='')
    estado = models.CharField(max_length=2, choices=ESTADOS, verbose_name='Estado', null=True, blank=True, default='PI')

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.email

    def get_categoria_pessoa(self):
        return list(filter(lambda c: c[0] == self.categoria_pessoa, CATEGORIA_PESSOA))[0][1]
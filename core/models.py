from django.db import models
from edital.models import Edital


class Contratante(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    sigla = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = 'Contratante'
        verbose_name_plural = 'Contratantes'

    def __str__(self):
        return self.nome


class PoloAtuacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao = models.TextField(verbose_name="Descrição", help_text='Adicione o endereço/telefones, horário de funcionamento')

    class Meta:
        verbose_name = 'Polo de Atuação'
        verbose_name_plural = 'Polos de Atuações'

    def __str__(self):
        return self.nome


class Documento(models.Model):
    ativo = models.BooleanField(default=True)
    ordem = models.IntegerField(null=True, default=1)
    titulo = models.CharField(max_length=250, verbose_name='Título', blank=False, null=True)
    documento = models.FileField(verbose_name="Documento", upload_to='documento_publico/%Y/%m/%d', blank=False, null=True)
    edital = models.ForeignKey(Edital, verbose_name='Edital', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def get_absolute_url(self):
        return self.documento.url

    def __str__(self):
        return self.titulo


class DocumentoUsuario(models.Model):
    ativo = models.BooleanField(default=True)
    titulo = models.CharField(max_length=250, verbose_name='Título', blank=False, null=True)

    class Meta:
        verbose_name = 'Documento Pessoal do Usuario'
        verbose_name_plural = 'Documentos Pessoais dos Usuários'

    def get_absolute_url(self):
        return self.documento.url

    def __str__(self):
        return self.titulo


class Servico(models.Model):

    titulo = models.CharField('Título', max_length=240, null=True)
    codigo = models.CharField(max_length=250, verbose_name='Código', unique=True)
    polo_atuacao = models.ForeignKey(PoloAtuacao, on_delete=models.CASCADE, null=True, blank=False, editable=True, verbose_name='Polo de atuação')

    def __str__(self):
        return  '{} - {} / {}'.format(self.codigo, self.titulo, self.polo_atuacao.nome)


class Requisito(models.Model):
    titulo = models.CharField(max_length=250, verbose_name='Título do Documento', blank=False, null=True)
    descricao = models.TextField(verbose_name='Descrição do Documento', blank=True, null=True)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Documento Requisitado')

    class Meta:
        verbose_name = 'Documento Requisitado'
        verbose_name_plural = 'Documentos Requisitados'

    def __str__(self):
        return self.titulo
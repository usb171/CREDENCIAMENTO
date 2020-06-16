from django.db import models
from core.ferramentas.enumerate import STATUS_EDITAL, CATEGORIA_EDITAL, STATUS_INSCRICAO, STATUS_DOCUMENTO_REQUISITO_INSCRICAO
from private_storage.fields import PrivateFileField

def get_path_private(instance):
    return "/{}".format(instance.inscricao.usuario.id)

class Edital(models.Model):
    """
        *   Classe Edital
        *   Classe que destinado aos editais publicados
    """

    status = models.CharField(max_length=30, choices=STATUS_EDITAL, default='0')
    titulo = models.CharField(max_length=250, verbose_name='Título', null=True)
    codigo = models.CharField(max_length=250, verbose_name='Código', null=True)
    categoria = models.CharField(max_length=60, choices=CATEGORIA_EDITAL, verbose_name='Categoria')
    descricao = models.TextField(verbose_name="Descrição", null=True)
    contratante = models.ManyToManyField('core.contratante', related_query_name='+')
    servicos = models.ManyToManyField('core.servico', blank=True, related_query_name='+')
    data_publicacao = models.DateTimeField(verbose_name='Data de Publicação')
    ano_publicacao = models.CharField(max_length=5, verbose_name='Ano de Publicação', blank=True, null=True, editable=False)
    inicio_inscricao = models.DateTimeField(verbose_name='Inicio das Inscrições')
    fim_inscricao = models.DateTimeField(verbose_name='Fim das Inscrições')

    class Meta:
        # ordering = ['-id']
        verbose_name = 'Edital'
        verbose_name_plural = 'Editais'

    def save(self, *args, **kwargs):
        self.ano_publicacao = self.data_publicacao.strftime("%Y")
        super(Edital, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def get_categoria(self):
        return CATEGORIA_EDITAL[int(self.categoria)][1]

    def get_status(self):
        return STATUS_EDITAL[int(self.status)][1]


class Inscricao(models.Model):

    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_INSCRICAO, default='0', verbose_name='Status geral')
    servicos = models.ManyToManyField('core.Servico', blank=False)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

    def __str__(self):
        return self.usuario.email


class DocumentoRequisitoInscricao(models.Model):
    servico = models.ForeignKey('core.Servico', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100, choices=STATUS_DOCUMENTO_REQUISITO_INSCRICAO, default='0', verbose_name='Status do Documento')
    observacao = models.TextField(verbose_name='Observações', blank=True)
    inscricao = models.ForeignKey(Inscricao, on_delete=models.CASCADE, null=True, blank=False)
    requisito = models.ForeignKey('core.Requisito', on_delete=models.CASCADE, null=True, blank=False, editable=False)
    documento = PrivateFileField(verbose_name="Documento", upload_subfolder=get_path_private, blank=True, null=True)

    class Meta:
        verbose_name = 'Documento Requisitado'
        verbose_name_plural = 'Documentos Requisitados'

    def __str__(self):
        return  '{} / {}'.format(self.requisito.titulo, self.servico)
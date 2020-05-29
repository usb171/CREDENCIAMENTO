from django.db import models
from core.ferramentas.enumerate import STATUS_EDITAL, CATEGORIA_EDITAL


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
    # contratante = models.ManyToManyField('Contratante', related_query_name='+')
    # servicos = models.ManyToManyField(Servico, blank=True)
    # services = models.TextField(verbose_name="Descrição dos serviços")
    # polo_atuacao = models.ManyToManyField('PoloAtuacao', related_query_name='+')
    data_publicacao = models.DateTimeField(verbose_name='Data de Publicação')
    inicio_inscricao = models.DateTimeField(verbose_name='Inicio das Inscrições')
    fim_inscricao = models.DateTimeField(verbose_name='Fim das Inscrições')
    # tipo_docs = models.ManyToManyField(TipoDoc, verbose_name='Documento Requeridos', related_query_name='+')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Edital'
        verbose_name_plural = 'Editais'

    def __str__(self):
        return self.titulo

    def get_categoria(self):
        return CATEGORIA_EDITAL[int(self.categoria)][1]

    def get_status(self):
        return STATUS_EDITAL[int(self.status)][1]

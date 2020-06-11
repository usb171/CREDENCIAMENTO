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
    contratante = models.ManyToManyField('Contratante', related_query_name='+')
    # servicos = models.ManyToManyField(Servico, blank=True)
    # services = models.TextField(verbose_name="Descrição dos serviços")
    polo_atuacao = models.ManyToManyField('PoloAtuacao', related_query_name='+')
    data_publicacao = models.DateTimeField(verbose_name='Data de Publicação')
    ano_publicacao = models.CharField(max_length=5, verbose_name='Ano de Publicação', blank=True, null=True, editable=False)
    inicio_inscricao = models.DateTimeField(verbose_name='Inicio das Inscrições')
    fim_inscricao = models.DateTimeField(verbose_name='Fim das Inscrições')
    # tipo_docs = models.ManyToManyField(TipoDoc, verbose_name='Documento Requeridos', related_query_name='+')

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


class Requisito(models.Model):
    ativo = models.BooleanField(default=True)
    ordem = models.IntegerField(null=True, default=1)
    titulo = models.CharField(max_length=250, verbose_name='Título', blank=False, null=True)
    edital = models.ForeignKey(Edital, verbose_name='Edital', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Requisito'
        verbose_name_plural = 'Requisitos'

    def __str__(self):
        return self.titulo
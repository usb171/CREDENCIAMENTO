
__author__ = "Nilton Nonato Garcia Júnior"
__copyright__ = "Federação das Indústrias do Estado do Piauí - FIEPI"
__email__ = "nilton.pi.dev@gmail.com"
__license__ = "GNU General Public License"
__date__ = "27 de Maio de 2020"
__version__ = "1.0.0"

ESTADOS = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande Do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)


STATUS_EDITAL = (
    ('0', 'Rascunho'),
    ('1', 'Publicado'),
    ('2', 'Cancelado'),
    ('3', 'Encerrado'),
)

STATUS_INSCRICAO = (
    ('0', 'Em Análise'),
    ('1', 'Inabilitada'),
    ('2', 'Habilitada'),
    ('3', 'Expirada'),
    ('4', 'Descredenciada'),
)

STATUS_DOCUMENTO_REQUISITO_INSCRICAO = (
    ('0', 'Em Análise'),
    ('1', 'Documento OK'),
    ('2', 'Documento Vencido'),
    ('3', 'Documento Ilegível'),
    ('4', 'Documento Inválido'),
)

CATEGORIA_EDITAL = (
    ('0', 'Pessoa Física'),
    ('1', 'Pessoa Jurídica'),
    ('2', 'Pessoa Física/Jurídica')
)

CATEGORIA_PESSOA = (
    ('0', 'Pessoa Física'),
    ('1', 'Pessoa Jurídica'),
)

SEXO = {
    ('0', 'Masculino'),
    ('1', 'Feminino'),
}
from django.urls import path
from .views import Core, CoreAjax

urlpatterns = [
    path('', Core.index, name='index'),
    path('get_edital_descricao_ajax', CoreAjax.get_edital_descricao, name='get_edital_descricao_ajax'),
    path('get_editais_filtros_ajax', CoreAjax.get_editais_filtros, name='get_editais_filtros_ajax'),
    path('validar_login_usuario', CoreAjax.validar_login_usuario, name='validar_login_usuario'),

    path('login', Core.login, name='login'),
    path('logout', Core.logout, name='logout'),
    path('usuario/novoUsuario', Core.novoUsuario, name='novoUsuario'),
    path('usuario/editarMeusDados', Core.editarMeusDados, name='editarMeusDados'),

    path('buscarEmailAjax', CoreAjax.buscarEmail, name='buscarEmailAjax'),
    path('buscarCpfAjax', CoreAjax.buscarCpf, name='buscarCpfAjax'),
    path('buscarCnpjAjax', CoreAjax.buscarCnpj, name='buscarCnpjAjax'),

    path('cancelarDocumentoRequisitoAjax', CoreAjax.cancelar_documento_requisito, name='cancelarDocumentoRequisitoAjax'),
    path('cancelarDocumentoUsuarioAjax', CoreAjax.cancelar_documento_usuario, name='cancelarDocumentoUsuarioAjax'),

    path('getBlocosCamposArquivosServicosAjax', CoreAjax.get_blocos_campos_arquivos_servicos, name='getBlocosCamposArquivosServicosAjax'),


]

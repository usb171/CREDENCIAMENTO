//jQuery(document).ready(function() {
    const buscarEditais = (carregar=true) => {
        let select_ano = $("#id_select_ano").val();
        let select_categoria = $("#id_select_categoria").val();
        let html_cursos = '';

        if(carregar){
            EasyLoading.show({
                type: EasyLoading.TYPE["BALL_PULSE"],
                text: 'Buscando Editais',
                timeout: null,
            });
            $.ajax({
                type: "GET",
                url: `get_editais_filtros_ajax?ano=${select_ano}&categoria=${select_categoria}`,
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function(data) {
                    if(data["editais"].length){
                        $("#id_lista_editais").html(data["editais"]);
                    }else{
                        $("#id_lista_editais").html("<h5 style='text-align: center;margin-top: 30px;'> Não foram encontrados editais, verifique os filtros acima!</h5>");
                    }
                    EasyLoading.hide();
                },
                error: function(data) {
                    EasyLoading.hide();
                }
            });
        }
    };

    const abrirDescricaoEdital = (id) => {
        EasyLoading.show({
                type: EasyLoading.TYPE["BALL_PULSE"],
                text: 'Abrindo Edital...',
                timeout: null,
        });

        $.ajax({
            type: "GET",
            url: "get_edital_descricao_ajax?id=" + id,
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(data) {
                $("#descricao_modal").modal('show');
                EasyLoading.hide();
                $("#id_modal_body_edital_descricao").html(data['descricao']);
            },
            error: function(data) {
                EasyLoading.hide();
            }
        });
    };

    const validar_login_usuario_redirecionar_inscricao = (id) => {
        $.ajax({
            type: "GET",
            url: "validar_login_usuario",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(data) {
                if (data.login_flag == false){
                    $("#descricao_modal").modal('hide');
                    $("#login_modal").modal('show');
                    $("#id_inscricao").val(id);
                }else{
                    window.open("/edital/inscricao?id=" + id,"_self");
                }
            },
            error: function(data) {}
        });
    };

    $("#id_servicos_select2").select2({
        width: '100%',
        placeholder: "Selecione um ou mais serviços",
        closeOnSelect: false,
        "language": {
            "noResults": function(){
               return "Edital sem serviços";
            }
        },
    });

    $('#id_servicos_select2').on('select2:select', function (e) {
       let ids_selected = $(this).select2("val");
       let id_edital = getUrlVars().id;
       get_bloco_campos_arquivos_servico(ids_selected, id_edital);
    });

    $('#id_servicos_select2').on('select2:unselect', function (e) {
       let ids_selected = $(this).select2("val");
       id_edital = getUrlVars().id;
       get_bloco_campos_arquivos_servico(ids_selected, id_edital);
    });

    $('#id_servicos_select2').on('change.select2', function (e) {
       let ids_selected = $(this).select2("val");
       let id_edital = getUrlVars().id;
       get_bloco_campos_arquivos_servico(ids_selected, id_edital);
    });

    let get_bloco_campos_arquivos_servico = (ids, id_edital) => {
       $.ajax({
            url: "/getBlocosCamposArquivosServicosAjax",
            data: {'ids_selected': ids.join(), 'id_edital':  id_edital},
            dataType: 'json',
            success: function (data) {
                $("#id_blocos_servicos").html(data.blocos)
            }
        });
    };


    function getUrlVars() {
        /**
         * Esta função retorna as variáveis de um URL
         */
        var vars = {};
        var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) { vars[key] = value; });
        return vars;
    }

    let cancelar_documento = (id) => {
        $.ajax({
            url: "/cancelarDocumentoAjax",
            data: {'id': id},
            dataType: 'json',
            success: function (data) {
                let ids_selected = $(id_servicos_select2).select2("val");
                let id_edital = getUrlVars().id;
                get_bloco_campos_arquivos_servico(ids_selected, id_edital);
                console.log(data);
                window.location='inscricao?id=' + getUrlVars().id;
            }
        });
    };

     $("#id_servicos_select2").val(JSON.parse($("#id_servicos_select2_val").val())).trigger('change');


//});

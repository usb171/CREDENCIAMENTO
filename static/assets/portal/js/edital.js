
//const carregarFiltros = () => {
//    let select_ano = $("#id_select_ano");
//    let select_categoria = $("#id_select_categoria");
//
//    $.ajax({
//        type: "GET",
//        url: "/API_SGE_CARREGAR_FILTROS",
//        contentType: "application/json; charset=utf-8",
//        dataType: "json",
//        success: function(data) {
//            select_ano.html(data.areas);
//            select_categoria.html(data.cidades);
//        },
//        error: function(data) {}
//    });
//};

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
            console.log(data)
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

//$('#login_modal').on('hidden.bs.modal', function () {
//      $("#descricao_modal").modal('show');
//});



const carregarFiltros = () => {
    let select_ano = $("#id_select_ano");
    let select_categoria = $("#id_select_categoria");

    $.ajax({
        type: "GET",
        url: "/API_SGE_CARREGAR_FILTROS",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data) {
            select_ano.html(data.areas);
            select_categoria.html(data.cidades);
        },
        error: function(data) {}
    });
};

const buscarEditais = (carregar=true) => {
    let cidade = $("#id_select_cidade").val();
    let area = $("#id_select_area").val();
    let turno = $("#id_select_turno").val();
    let modalidade = $("#id_select_mediacao").val();
    let html_cursos = '';

    if(carregar){
        EasyLoading.show({
            type: EasyLoading.TYPE["BALL_PULSE"],
            text: 'Buscando Editais',
            timeout: null,
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
            url: "get_edital_ajax?id=" + id,
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

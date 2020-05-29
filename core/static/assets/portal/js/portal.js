let owl_top_carousel = $('#id_top_carousel');
owl_top_carousel.owlCarousel({
    items:1,
    loop:true,
    margin:10,
    autoplay:true,
    autoplayTimeout:3000,
    autoplayHoverPause:false,
    autoWidth:false,
    autoHeight:true,
    responsiveClass:true,
});

let owl_carousel_propaganda = $('#id_carousel_propaganda');
owl_carousel_propaganda.owlCarousel({
    loop:true,
    dots:true,
    margin:10,
    autoplay:true,
    autoplayTimeout:5000,
    autoplayHoverPause:false,
    animateOut: 'fadeOut',
    responsive:{
       0:{
            items:1
       },
       600:{
            items:2
       },
       960:{
            items:3
       },
       1200:{
            items:4
       }
    }
});

let owl_carousel_servicos_1 = $('#id_carousel_servicos_1');
owl_carousel_servicos_1.owlCarousel({
    items:1,
    loop:true,
    margin:10,
    autoplayHoverPause:false,
    autoWidth:false,
    autoHeight:true,
    responsiveClass:true,
});

let owl_carousel_servicos_2 = $('#id_carousel_servicos_2');
owl_carousel_servicos_2.owlCarousel({
    items:1,
    loop:true,
    margin:10,
    autoplayHoverPause:false,
    autoWidth:false,
    autoHeight:true,
    responsiveClass:true,
});

let owl_top_carousel_noticias_destaque = $('#id_top_carousel_noticias_destaque');
owl_top_carousel_noticias_destaque.owlCarousel({
    loop:true,
    dots:true,
    margin:10,
    autoplay:false,
    animateOut: 'fadeOut',
    responsive:{
       0:{
            items:1
       },
       600:{
            items:2
       },
       960:{
            items:3
       },
       1200:{
            items:4
       }
    }
});

let owl_top_carousel_noticias_geral = $('#id_top_carousel_noticias_geral');
owl_top_carousel_noticias_geral.owlCarousel({
    loop:true,
    dots:true,
    margin:10,
    autoplay:false,
    animateOut: 'fadeOut',
    responsive:{
       0:{
            items:1
       },
       600:{
            items:2
       },
       960:{
            items:3
       },
       1200:{
            items:4
       }
    }
});


/**
 ** Funções para da busca do topo da página
 **/

function selectSuggest(d){
    $("#searchInput").val(d);
}

function displaySearchSuggest(e, a){


    if(a==1){

        let posicaoInput = $("#searchInput").offset()
        let widthInput = $("#searchInput").width()
        let searchSuggest = $($("#search_box_cover").children()[0])

        posicaoInput.top -= -39
        posicaoInput.left -= 0

        $($("#search_box_cover").children()[0]).offset(posicaoInput)
        searchSuggest.width(widthInput + 66)


        if($("#search_suggest_list").children().length != 0){
            $("#search_suggest_box").show();
        }

    }else{
        $("#search_suggest_box").hide(e=>{});
        $("#search_suggest_list").html();
        $('#searchInput').val('')

    }
}

$(document).ready(function(e) {
    $('#searchInput').focus(function(e) {displaySearchSuggest(1);});
    //$('#search_suggest_list').blur(function(e) {displaySearchSuggest(e, 0);});
    $('#wrapper').click(function(event){
        displaySearchSuggest(e, 0);
    });
});

window.addEventListener('error', function(e) {
    console.log(e);
}, true);

$('#searchInput').keyup(function(e){

    var $listItems = $('li.search_suggest_item');

    var key = e.keyCode,
    $selected = $listItems.filter('.selected'),
    $current;

    if( key === 13){
        $('li.search_suggest_item.selected').click()
    }

    if( key != 37 && key != 38 && key != 39 && key != 40 && key != 16 &&
        key != 17 && key != 18 && key != 19 &&
        key != 20 && key != 27 && key != 225){
        var valorBusca = this.value
        if(valorBusca.length >= 3){
            $("#search_suggest_list").html('<span style="color:blue;">Buscando Cursos...</span>');
            clearTimeout(this.interval)
            displaySearchSuggest(e, 1)
            this.interval = setTimeout(function(){

                    //$.get(`../../../../../../../API_SGE_BUSCAR_CURSO_NOME?curso=${valorBusca}&quantidade=20`, function( data ) {
                    $.get(`../../../../../../../BUSCA_NAVBAR?palavra=${valorBusca}&quantidade=20`, function( data ) {
                        $("#search_suggest_list").html(data.lista);
                        if(data.quantElementos === 0){
                            $("#search_suggest_list").html('<span style="color:blue;">Curso não encontrado.</span>');
                        }else if (data.Erro){
                            $("#search_suggest_list").html('<span style="color:blue;">'+ data.Erro +'</span>');
                        }
                    });

                    valorBusca = ''
            }, 200);
        }else{
           displaySearchSuggest(e, 1)
           $("#search_suggest_list").html('<span style="color:blue;">Caracteres insuficientes (' + valorBusca.length + '/3) </span>');
        }
    }

    if ( key != 40 && key != 38 ) return;

    $listItems.removeClass('selected');

    if ( key == 40 ) // Down key
    {
    if ( ! $selected.length || $selected.is(':last-child') ) {
        $current = $listItems.eq(0);
    }
    else {
        $current = $selected.next();
    }
    }
    else if ( key == 38 ) // Up key
    {
    if ( ! $selected.length || $selected.is(':first-child') ) {
        $current = $listItems.last();
    }
    else {
        $current = $selected.prev();
    }
    }
    $current.addClass('selected');

});





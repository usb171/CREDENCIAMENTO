$(function(){
    let campos = ['imagem', 'texto', 'youtube'];

    let esconder_campos = (id_bloco) => {

        $.each(campos, function( index, value ) {
            $("#bloconoticia_set-"+ id_bloco +" .field-" + value).hide()
        });
    }


    let init_bloco_noticia = (id_bloco) => {

        esconder_campos(id_bloco);

        $('#id_bloconoticia_set-'+ id_bloco +'-tipo_bloco').change(function(){
            let field = this.value;
            if (field == "texto"){
                $("#bloconoticia_set-"+ id_bloco +" .field-texto").show();
            }else if(field == "imagem"){
                $("#bloconoticia_set-"+ id_bloco +" .field-imagem").show();
            }else if(field == "youtube"){
                $("#bloconoticia_set-"+ id_bloco +" .field-youtube").show();
            }
        });
    }

    for (let id_bloco = 0; id_bloco < 10; id_bloco++){
        init_bloco_noticia(id_bloco);
    }

});
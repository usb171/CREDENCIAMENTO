$('#login').submit(function(e){
    e.preventDefault();
    $.post("/login", $(this).serialize(), function(data){
        console.log(data);
        if (data.logado){
            let id_inscricao = $("#id_inscricao").val();
            if(id_inscricao == ""){
                window.location='edital/minhasInscricoes';
            }else{
                window.location='edital/inscricao?id=' + id_inscricao;
            }
        }else{
             $.toast({
                    heading: data.msg,
                    icon: 'error',
                    position: 'top-right',
                    hideAfter: 6000,
                    showHideTransition: 'plain',
             })
        }
    }, 'json')
});

$('#id_form_novoUsuario').submit(function(e){
    e.preventDefault();
    $.post("/usuario/novoUsuario", $(this).serialize(), function(data){
        if (data.status){
//            $.toast({
//                heading: 'Cadastro Realizado com Sucesso!',
//                icon: 'success',
//                position: 'top-right',
//                hideAfter: 3000,
//                showHideTransition: 'plain',
//            });
            window.location='edital/minhasInscricoes';
        }else{
            let keys = Object.keys(data.erros);
            $.each(keys, (index, key) => {
                $.toast({
                    heading: data.erros[key],
                    icon: 'error',
                    position: 'top-right',
                    hideAfter: 6000,
                    showHideTransition: 'plain',
                })
                $("#" + key).removeClass("is-valid").addClass("is-invalid");
            });
        }
    }, 'json')
});


$('#id_form_meus_dados_pessoa_fisica').submit(function(e){

    console.log('Aqui');

    e.preventDefault();
    $.post("/usuario/editarMeusDados", $(this).serialize(), function(data){
        if (data.status){
            window.location='minhasInscricoes';
        }else{
            let keys = Object.keys(data.erros);
            $.each(keys, (index, key) => {
                $.toast({
                    heading: data.erros[key],
                    icon: 'error',
                    position: 'top-right',
                    hideAfter: 6000,
                    showHideTransition: 'plain',
                })
                $("#" + key).removeClass("is-valid").addClass("is-invalid");
            });
        }
    }, 'json')
});



$('#email').keyup(function(event) {
    $.ajax({
        url: "../buscarEmailAjax",
        data: {'email': $(this).val()},
        dataType: 'json',
        success: function (data) {
            if (data.flag){
                $("#email").removeClass("is-valid").addClass("is-invalid");
                $("#email")[0].setCustomValidity("Email já Cadastrado");
            }
            else{
                $("#email").removeClass("is-invalid").addClass("is-valid");
                $("#email")[0].setCustomValidity('');
            }
        }
    });
});

$('#cpf').keyup(function(event) {

    $.ajax({
        url: "../buscarCpfAjax",
        data: {'cpf': $(this).val()},
        dataType: 'json',
        success: function (data) {
            if (data.flag){
                $("#cpf").removeClass("is-valid").addClass("is-invalid");
                $("#cpf")[0].setCustomValidity("CPF já Cadastrado");
            }
            else{
                $("#cpf").removeClass("is-invalid").addClass("is-valid");
                $("#cpf")[0].setCustomValidity('');
            }
        }
    });
});

$('#cnpj').keyup(function(event) {

    $.ajax({
        url: "../buscarCnpjAjax",
        data: {'cnpj': $(this).val()},
        dataType: 'json',
        success: function (data) {
            if (data.flag){
                $("#cnpj").removeClass("is-valid").addClass("is-invalid");
                $("#cnpj")[0].setCustomValidity("CNPJ já Cadastrado");
            }
            else{
                $("#cnpj").removeClass("is-invalid").addClass("is-valid");
                $("#cnpj")[0].setCustomValidity('');
            }
        }
    });
});

$('#select_categora_pessoa').change(function() {
    let cpf = $("#cpf");
    let cnpj = $("#cnpj");
    let nome = $("#nome");
    let cnpj_cpf = $("#cnpj_cpf");
    let razaoSocial = $("#razaoSocial");
    let nomeFantasia = $("#nomeFantasia");
    let nomeResponsavel = $("#nomeResponsavel");
    let cnpjResponsavel = $("#cnpj_responsavel");
    let categoria_pessoa = $("#categoria_pessoa").val();
    let div_campos = $("#id_campos_novo_cadastro");

    div_campos.show();

    if(categoria_pessoa == '0'){ // Pessoa Física
        nome.removeAttr('disabled').val("").attr('required', 'required');
        cpf.removeAttr('disabled').val("").attr('required', 'required');
        cnpj.attr('disabled', 'disabled').val("");
        cnpj_cpf.attr('disabled', 'disabled').val("");
        razaoSocial.attr('disabled', 'disabled').val("");
        nomeFantasia.attr('disabled', 'disabled').val("");
        nomeResponsavel.attr('disabled', 'disabled').val("");
        cnpjResponsavel.attr('disabled', 'disabled').val("");

    }else if(categoria_pessoa == '1'){ // Pessoa Jurídica
        nome.attr('disabled', 'disabled').val("").removeAttr('required');
        cpf.attr('disabled', 'disabled').val("").removeAttr('required');
        cnpj.removeAttr('disabled').val("").attr('required', 'required');
        cnpj_cpf.removeAttr('disabled').val("").attr('required', 'required');
        razaoSocial.removeAttr('disabled').val("").attr('required', 'required');
        nomeFantasia.removeAttr('disabled').val("").attr('required', 'required');
        nomeResponsavel.removeAttr('disabled').val("").attr('required', 'required');
        cnpjResponsavel.removeAttr('disabled').val("").attr('required', 'required');
    }else{
        div_campos.hide();
    }
});

$("#id_campos_novo_cadastro").hide();
$('#formNovoFilme').bind("submit", (event) => {
    event.preventDefault();
    let urlAction = $('#formNovoFilme').prop('action');

    let filme = montaObjetoDeSerializeArray($('#formNovoFilme').serializeArray());
    console.log(filme);
    console.log(urlAction);
    
    $.post({
        url:urlAction, 
        dataType:'json', 
        data:JSON.stringify(filme), 
        contentType: "application/json",
        error: e => {
            console.log(e.responseJSON)
        }
    }, result => {
        //adicionaClienteTabela(result);
        let alerta = $('#infoSemCliente');
        if (alerta) {
            alerta.remove();
        }
    });

    $('#formNovoFilme').collapse('toggle');
});

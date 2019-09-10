console.log('Locadora JS carregado.');
console.log($('#formNovoCliente').prop('action'));
/*{email: "cezar_andrade_10@hotmail.com", id: 11, nome: "Castlevania", telefone: "3774-8342"} */

function montaCliente (dados){
    let cliente = {}
    dados.forEach(element => {
        let chave = element.name
        cliente[chave] = element.value
    });
    return cliente
}

function montaTd(dado) {
    var td = document.createElement('td');
    td.textContent = dado;
    return td
}

function montaTr(cliente){

    var tr = document.createElement('tr');

    tr.appendChild(montaTd(cliente.id));
    tr.appendChild(montaTd(cliente.nome));
    tr.appendChild(montaTd(cliente.email));
    tr.appendChild(montaTd(cliente.telefone));

    return tr
}

function adicionaClienteTabela(cliente) {

    var clienteTr = montaTr(cliente);

    $('#tabelaClientes').append(clienteTr);
}

$('#formNovoCliente').on("submit", (event) => {
    event.preventDefault();
    let urlAction = $('#formNovoCliente').prop('action');

    let cliente = montaCliente($('form').serializeArray());

    $.post({
        url:urlAction, 
        dataType:'json', 
        data:JSON.stringify(cliente), 
        contentType: "application/json",
        error: e => {
            console.log(e.responseJSON)
        }
    }, result => {
        adicionaClienteTabela(result);
    });

});
/*{email: "cezar_andrade_10@hotmail.com", id: 11, nome: "Castlevania", telefone: "3774-8342"} */
function criaBotaoRemover(id){
    let botao = document.createElement('a');
    let urlRef = $('#formNovoCliente').attr('action');
    
    botao.setAttribute('href', `${urlRef}/${id}`);
    botao.classList.add('botaoRemover');
    botao.text = 'Remover';

    return botao
}

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
    td.append(dado);
    return td
}

function montaTr(cliente){

    var tr = document.createElement('tr');

    tr.appendChild(montaTd(cliente.id));
    tr.appendChild(montaTd(cliente.nome));
    tr.appendChild(montaTd(cliente.email));
    tr.appendChild(montaTd(cliente.telefone));
    tr.appendChild(montaTd(criaBotaoRemover(cliente.id)));

    return tr
}

function adicionaClienteTabela(cliente) {

    var clienteTr = montaTr(cliente);

    $('#tabelaClientes').append(clienteTr);
}

$('#formNovoCliente').bind("submit", (event) => {
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
        let alerta = $('#infoSemCliente');
        if (alerta) {
            alerta.remove();
        }
    });

    $('#formNovoCliente').collapse('toggle');

});

function popConfirma(cliente){
    return confirm(`Você realmente gostaria de REMOVER o ${cliente.nome} ?`);
}

function criaCliente(listaValues) {
    let cliente = {}
    cliente.id = listaValues[0]
    cliente.nome = listaValues[1]
    cliente.email = listaValues[2]
    cliente.telefone = listaValues[3]

    return cliente
}

function setAttributes(el, attrs) {
    for(var key in attrs) {
      el.setAttribute(key, attrs[key]);
    }
}

function criaBotaoDismiss () {
    var botaoDismiss = document.createElement('button');
    var span = document.createElement('span');
    
    botaoDismiss.classList.add('close');
    setAttributes(botaoDismiss, {'type':'button', 'data-dismiss':'alert', 'aria-label':'Close'});

    span.setAttribute('aria-hidden', 'true');
    span.innerHTML = '&times;';

    botaoDismiss.append(span);

    return botaoDismiss;    
}

function atualizaCliente(cliente) {
    let tr = $('#tabelaClientes').find(`td:contains(${cliente.id})`).parent();
    console.log(tr);
    (tr.children('[name]')).each( (index, td) => {
        $(td).text(cliente[$(td).attr('name')]);
    });
}

$('#tabelaClientes').on('click', '.botaoRemover', function(clicado) {
    urlRemover = $(clicado.target).attr("href");

    var listCliente = [];
    $(clicado.target).parent().parent().children('td').text(function(index, campo){
        listCliente.push(campo);
    });
    var cliente = criaCliente(listCliente);
    if (!popConfirma(cliente)){
        return false;
    }
    $.ajax({
        url: urlRemover,
        type: 'DELETE',
        success: function(){
            var alerta = criaAlerta(`${listCliente[1]} Removido!`, `O cliente de email ${listCliente[2]} foi removido.`);
            adicionarTempAlerta(alerta, 15);
            $(clicado.target).parent().parent().remove()
        },
        error: function(){
            var alerta = criaAlerta('Há algo errado com o servidor. Tente novamente.');
            adicionarTempAlerta(alerta, 15);
        }
    });

    return false
});
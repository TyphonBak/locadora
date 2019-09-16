function alteraClienteAPI (cliente) {
    let urlRef = $('#formAlterarCliente').attr('action');
    var mensagem = '';
    $.ajax({
        url: urlRef,
        type: 'PUT',
        data: JSON.stringify(cliente),
        contentType: 'application/json'
    })
    .done( function(result) {
        mensagem = [`Novos dados: ${result.nome}, ${result.email}, ${result.telefone}`, `Alterados de: ${cliente.nome}, ${cliente.email}, ${cliente.telefone}`];
        return mensagem;
    })
    .fail( function(e) {
        console.log(e);
        mensagem = ['Erro!', 'Algo de errado não está certo. Tente Novamente.'];
        return mensagem;
    })
    .then(function (result) {
        var alerta = criaAlerta(mensagem[0], mensagem[1]);
        adicionarTempAlerta(alerta, 20);
        atualizaCliente(result);
        $('#modalAlterar').modal('hide');
    });
}

$('#botaoSalvarAlteracoes').on('click', () => {
    let cliente = montaCliente($('#formAlterarCliente').serializeArray());
    console.log(cliente);
    alteraClienteAPI(cliente);
})

$('#modalAlterar').on('show.bs.modal', target => {
    const botao = $(target.relatedTarget);
    let listCliente = []
    botao.parent().parent().children('td').text(function(index, campo){
        if ($.inArray(index, [0,1,2,3]) != -1) {
            listCliente.push(campo);
        }
    });
    let cliente = criaCliente(listCliente);
    
    const modal = $('#modalAlterar');

    let nomeInput = modal.find(`[id=nomeClienteAlterar]`)
    let emailInput = modal.find(`[id=emailClienteAlterar]`)
    let telefoneInput = modal.find(`[id=telefoneClienteAlterar]`)

    nomeInput.val(cliente.nome)
    emailInput.val(cliente.email)
    telefoneInput.val(cliente.telefone)

    $("#formAlterarCliente").prop('action', $('#formNovoCliente').attr('action') + `/${cliente.id}`);
})
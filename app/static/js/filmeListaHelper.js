function popConfirma(filme){
    return confirm(`Você realmente gostaria de REMOVER o filme ${filme.titulo} ?`);
}

function montaFilmeDeCard(card) {
    let camposNomeados = card.find('[name]')
    let filme = {}
    camposNomeados.each((index, campo) => {
        filme[$(campo).attr('name')] = $(campo).text();
    });
    return filme
}

function montaFilmeDeLista(lista) {
    let filme = {}
    filme.id = lista[0]
    filme.titulo = lista[0]
    filme.ano = lista[0]
    filme.genero = lista[0]
    filme.preco = lista[0]
    filme.estoque = lista[0]
    filme.sinopse = lista[0]
    filme.classificacao = lista[0]
    filme.diretor = lista[0]

    return filme
}

function preencheModalFilme(idModal, filme) {
    let modal = $(`#${idModal}`);

    let campoId = modal.find('[id=campoIdAlterar]')
    let campoTitulo = modal.find(`[id=campoTituloAlterar]`)
    let campoDiretor = modal.find(`[id=campoDiretorAlterar]`)
    let campoAno = modal.find(`[id=campoAnoAlterar]`)
    let campoGenero = modal.find(`[id=campoGeneroAlterar]`)
    let campoClassificacao = modal.find(`[id=campoClassificacaoAlterar]`)
    let campoPreco = modal.find(`[id=campoPrecoAlterar]`)
    let campoEstoque = modal.find(`[id=campoEstoqueAlterar]`)
    let campoSinopse = modal.find(`[id=campoSinopseAlterar]`)

    campoId.text(filme.id)
    campoTitulo.val(filme.titulo)
    campoDiretor.val(filme.diretor)
    campoAno.val(filme.ano)
    campoGenero.val(filme.genero)
    campoClassificacao.val(filme.classificacao)
    campoPreco.val(filme.preco)
    campoEstoque.val(filme.estoque)
    campoSinopse.val(filme.sinopse)

    return modal
}

function atualizaFilme(filme) {
    let card = $('#listaFilmes').find(`span:contains(${filme.id})`).parent().parent()
    (card.find('[name]')).each( (index, elem) => {
        $(elem).text(filme[$(elem).attr('name')]);
    });
}

function alteraFilmeAPI (filme) {
    let urlRef = $('#formAlteraFilme').attr('action');
    var mensagem = '';
    $.ajax({
        url: urlRef,
        type: 'PUT',
        data: JSON.stringify(filme),
        contentType: 'application/json'
    })
    .done( function(result) {
        mensagem = [`Sucesso!`, `Nome atual do filme alterado: ${result.titulo}`];
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
        atualizaFilme(result);
        $('#modalAlterarFilme').modal('hide');
    });
}

$('#listaFilmes').on('click', '.botaoRemoverFilme', clicado => {
    clicado.preventDefault();
    let urlRef = $(clicado.target).parent().prop('href');
    let card = $(clicado.target).parent().parent().parent().parent();
    let filme = montaFilmeDeCard(card);
    var mensagem = '';
    if (popConfirma(filme)) {
        $.ajax({
            url: urlRef,
            type: 'DELETE'
        })
        .done( () => {
            mensagem = ['Removido!', `O filme ${filme.titulo} foi removido com sucesso.`];
            return mensagem
        })
        .fail( () => {
            mensagem = ['Erro!', 'Algo de errado não está certo. Tente Novamente.'];
            return mensagem
        })
        .then( () => {
            let alerta = criaAlerta(mensagem[0], mensagem[1]);
            adicionarTempAlerta(alerta, 15);
        })
    }
    return false

});

$('#modalAlterarFilme').on('show.bs.modal', target => {
    const botao = $(target.relatedTarget);
    let card = $(botao).parent().parent().parent().parent();
    let filme = montaFilmeDeCard(card);
    
    preencheModalFilme('modalAlterarFilme', filme);

    $("#formAlteraFilme").prop('action', $('#formNovoFilme').attr('action') + `/${filme.id}`);
})

$('#botaoSalvarAlteracoes').on('click', () => {
    let filme = montaObjetoDeSerializeArray($('#formAlteraFilme').serializeArray());
    filme.id = $('#formAlteraFilme').find('[id=campoIdAlterar]').text();
    alteraFilmeAPI(filme);
})
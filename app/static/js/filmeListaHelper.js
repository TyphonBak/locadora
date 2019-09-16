function montaFilmeDeCard(dados) {
    console.log(dados)
    let filme = {}
    dados.each((index, dado) => {
        filme[$(dado).attr('name')] = $(dado).text();
    });
    return filme
}

function montaFilmeDeLista(dados) {
    let filme = {}
    filme.id = dados[0]
    filme.titulo = dados[0]
    filme.ano = dados[0]
    filme.genero = dados[0]
    filme.preco = dados[0]
    filme.estoque = dados[0]
    filme.sinopse = dados[0]
    filme.classificacao = dados[0]
    filme.diretor = dados[0]

    return filme
}

$('#listaFilmes').bind('click', '.botaoRemoverFilme', clicado => {
    clicado.preventDefault();
    let urlRef = $(clicado.target).parent().prop('href');
    let card = $(clicado.target).parent().parent().parent().parent();
    console.log(montaFilmeDeCard(card.find('[name]')));
    if (confirm('')) {
        $.ajax({
            url: urlRef,
            type: 'DELETE'
        })
        .done( result => {
            console.log(result);
        })
        .fail( result => {
            console.log(result);
    
        })
    }
    return false

});
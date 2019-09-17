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

function criaAlerta(destaque=null, message){
    var alertaDiv = document.createElement('div');
    var botaoDismiss = criaBotaoDismiss();

    if (destaque != null) {
        var textoDestaque = document.createElement('strong');    
        textoDestaque.textContent = `${destaque} \ `;
    }else {
        textoDestaque = '';
    }

    alertaDiv.classList.add('alert', 'alert-warning', 'alert-dismissible', 'fade', 'show', 'd-block');
    alertaDiv.setAttribute('role', 'alert');
    alertaDiv.append(textoDestaque);
    alertaDiv.append(`${message}`);
    alertaDiv.append(botaoDismiss);

    return alertaDiv;
}

function adicionarTempAlerta(alerta, segundos) {
    $('#areaInfo').append(alerta);

    setTimeout(function(){
        $(alerta).alert('close');
        $(alerta).alert('dispose');
    }, segundos*1000);

}

function montaObjetoDeSerializeArray (dados){
    let objeto = {}
    dados.forEach(element => {
        if (element.name){
            let chave = element.name
            objeto[chave] = element.value
        }
    });
    return objeto
}
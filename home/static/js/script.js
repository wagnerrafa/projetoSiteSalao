
function abrirMenu(){
    let menu = document.querySelector(".navbar");
    menu.classList.toggle('menu-toogle');
}

let posAnterior = window.pageYOffset;
let menu = document.querySelector(".menu");

window.onscroll = function () {
    let posAtual = window.pageYOffset;
    posAnterior > posAtual ? menu.style.top = "0" : menu.style.top = "-380px";
    posAnterior = posAtual;
}

document.addEventListener("DOMContentLoaded", function() {
    var conteudo = encodeURIComponent(document.title + " " + window.location.href);
    document.getElementById("whatsImg").href = "https://api.whatsapp.com/send?text=" + conteudo
}, false);


var cont =1;
var contAuto = cont;
var fim = document.querySelector(".contarPromo").innerText;

function preExibir(){ 
    document.getElementById('url-'+contAuto).click();
    contAuto++;
    if(contAuto > fim){
        contAuto=1;
    }
}

function proximaPromo(me){
    document.getElementById("wall-"+cont).style.display = 'none';

    if(me == "voltar"){
        cont--;
    }
    else{
        cont++;
    }
    if(cont > fim){
        cont=1;
    }
    if(cont == 0){
        cont = fim;
    }
    let idWall = "wall-"+cont;
    document.getElementById(idWall).style.display = 'block';
}

function carregarResposta(){
    document.querySelector(".sk-cube-grid").style.display = 'block';
    var resposta = document.querySelector(".resposta").innerHTML
    while(resposta == "a")
    {
        carregarResposta();
    }
    document.querySelector(".sk-cube-grid").style.display = 'none';
}

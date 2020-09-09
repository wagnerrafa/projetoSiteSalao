
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
if(me == "voltar"){
    document.getElementById("wall-"+cont).className = "wallRight";
}
else{
    document.getElementById("wall-"+cont).className = "wallLeft";
}
    let teste = document.getElementById("wall-"+cont);

    setTimeout( function() {
        teste.className = "wallOff";
    }, 1000 );  

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
    
    setTimeout( function() {
        document.getElementById(idWall).className = "wallOn"
    }, 1000 ); 
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

function abrirDesc(id){
    id -=1;
    document.querySelectorAll(".descricaoPromocao")[id].style.display = 'flex';
    document.querySelectorAll(".infoPromo")[id].style.display = 'none';
}
function fecharDesc(id){
    id -=1;
    document.querySelectorAll(".infoPromo")[id].style.display = 'block';
    document.querySelectorAll(".descricaoPromocao")[id].style.display = 'none';
}

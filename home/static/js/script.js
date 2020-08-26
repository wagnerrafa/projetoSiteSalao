// window.location = "#wall-1"

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

var i=1;

function esconderWall(){
    if(i==1){
    // document.querySelector(".wall-1").style.display = 'none';
    document.querySelector(".wall-1").className = 'wall';
    i++;
    }
}


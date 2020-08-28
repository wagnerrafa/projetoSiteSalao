
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



var verExecutado = false;
function esconderWall(){
    if(verExecutado == false){
    document.querySelector(".wall-1").classList = 'wall';
    verExecutado = true;
    }
}

var a =1;
var fim = document.querySelector(".contarPromo").innerText;

function preExibir(){ 
    esconderWall();        
    document.getElementById('url-'+a).click();
    a++;
    if(a > fim){
        a=1;
    }
    }




function abrirMenu(){
    let menu = document.querySelector(".navbar");
    menu.classList.toggle('menu-toogle');
}

let posAnterior = window.pageYOffset;
let menu = document.querySelector('.navbar');
window.onscroll = function () {
    let posAtual = window.pageYOffset;
    posAnterior > posAtual ? menu.style.top = "0" : menu.style.top = "-70px";
    posAnterior = posAtual;
}

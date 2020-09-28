/* funcao do menu mobile*/
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

/* Carrosel de fotos da pagina inicial*/
var imageCount = 0;
var currentImage = 1;
var imagemUrl = new Array();
var imagemTamanho = "";
onload=carregarImagem();
function carregarImagem(){
    imagemTamanho = document.getElementById("slideFoto-1").className;
   
    for(i = 1; i <= imagemTamanho;i++){
        imagemUrl[i] = document.getElementById("slideFoto-"+i).currentSrc;
    }
    var preLoadImages = new Array();
    for (var i = 1; i <= imagemUrl.length; i++){
        if (imagemUrl[i] == "")
            break;
    
    preLoadImages[i] = new Image();
    preLoadImages[i].src = imagemUrl[i];
    imageCount++;
    }
    startSlideShow();

}


function startSlideShow()
{
   if (document.body && imageCount > 0)
   {   
        document.getElementById("slideinicial").style.background = `linear-gradient(rgba(0,0,0,.2), rgba(0,0,0,.2)), url(${imagemUrl[currentImage]})`;
        document.getElementById("slideinicial").style.backgroundSize = "cover";
        document.getElementById("slideinicial").style.backgroundRepeat = "no-repeat";
        document.getElementById("slideinicial").style.backgroundPosition = "center"
        document.getElementById("slideinicial").style.backgroundAttachment = "fixed";

      currentImage = currentImage + 1;
      if (currentImage > (imageCount-1))
      { 
         currentImage = 1;
      }
      setTimeout('startSlideShow()', 4000);
   }
}

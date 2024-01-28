var i = 0;
var imagenes = ["img/fondo_tocadiscos.jpg", "img/fondo_receiver.jpg", "img/fondo_radio.jpg"]
var imagen = document.getElementById("imagenf");

function cambioimg (){
    imagen.style.opacity = 0.75;

    setTimeout(function(){
        imagen.src = imagenes[i];
        imagen.style.opacity = 1;
        i = (i+1) % imagenes.length;
    },120);
}

function nuevaimg(){
    cambioimg ()
    setInterval(cambioimg,3000);
}

window.onload = function(){
    nuevaimg();
};
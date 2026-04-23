let fondo = document.querySelector('.fondo');
let animacion = false;
let fondoBajo= document.querySelector('.fondo-bajo')

function updatefondo(){
    let moveY = window.scrollY;
    let maxScroll = 400;
    let movimiento = Math.min(moveY / maxScroll,1);
    let escala = 1 + movimiento * 5;
    let opacidad = 1 - movimiento;

    fondo.style.transform = `scale(${escala})`;
    fondo.style.opacity = opacidad;
    animacion = false;
}
window.addEventListener('scroll', ()=>{

    if(!animacion){
        animacion = true;
        requestAnimationFrame(updatefondo);
    }
})

function updatefondobajo() {
    let moveY = window.scrollY;
    let maxScroll = 400;
    let movimiento = Math.max(moveY / maxScroll,1);
    let escala = 1 + movimiento * 5;
    let opacidad = 1 - movimiento;

    fondoBajo.style.transform = `scale(${escala})`;
    fondoBajo.style.opacity = opacidad;
    animacion = false;
}
window.addEventListener('scroll', ()=>{
    if(!animacion){
        animacion = true;
        requestAnimationFrame(updatefondobajo);
    }
})
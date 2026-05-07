let fondo = document.querySelector(".fondo");
let animacion = false;
// let fondoBajo = document.querySelector(".fondo-bajo");

function updateFondo() {
  let moveY = window.scrollY;
  let maxScroll = 400;
  let movimiento = Math.min(moveY / maxScroll, 1); //  Math.min()Esta función elige el número más pequeño entre el resultado y 1. Sirve para que, aunque bajes 1000px, el valor de movimiento nunca sea mayor a 1 (100%). 
  //moveY / maxScroll Divide lo que has bajado entre el máximo (400px). Esto crea un porcentaje de 0 a 1.
  let escala = 1 + movimiento * 5;
  let opacidad = 1 - movimiento;

  fondo.style.transform = `scale(${escala})`;
  fondo.style.opacity = opacidad;
  animacion = false;
}
window.addEventListener("scroll", () => {
  if (!animacion) {
    animacion = true;
    requestAnimationFrame(updateFondo);
  }
});

// function updatefondobajo() {
//   let moveY = window.scrollY;
//   let maxScroll = 400;
//   let movimiento = Math.max(moveY / maxScroll, 1);
//   let escala = 1 + movimiento * 5;
//   let opacidad = 1 - movimiento;

//   fondoBajo.style.transform = `scale(${escala})`;
//   fondoBajo.style.opacity = opacidad;
//   animacion = false;
// }
// window.addEventListener("scroll", () => {
//   if (!animacion) {
//     animacion = true;
//     requestAnimationFrame(updatefondobajo);
//   }
// });

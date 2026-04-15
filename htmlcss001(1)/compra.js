let boton = document.getElementById("boton-compra")
let texto = document.getElementById("texto-pagar")

function mostrarColor(){
    texto.innerText = "¡Gracias por su compra!"
    texto.style.color = "green"
    boton.innerText = "Comprado"
    

}

boton.addEventListener("click", mostrarColor)
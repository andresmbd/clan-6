def buscar(n: int, lista: list):
    izq = 0
    der = len(lista) - 1
    encontrado = False

    while encontrado == False and izq <= der:
        cen = (izq + der) // 2

        if lista[cen] == n:
            encontrado = True

        elif lista[cen] < n:
            izq = cen + 1 # para descartar la posición del centro y la parte izquierda, luego rodarlo una posicion +
        
        else:
            der = cen - 1 # para descartar la posición del centro y la parte derecha, luego rodarlo una posicion -

    if encontrado == True:
        print("Encontrado, posición:", cen)
    else:
        print("No se encontró el número")


op = ""
numeros = [2, 5, 8, 17, 32, 55, 130, 200]

while op != "no":
    entrada = int(input("Número del array: "))
    buscar(entrada, numeros)

    op = input("¿Elegir otro número? (si/no): ").lower()

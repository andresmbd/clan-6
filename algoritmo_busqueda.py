    
op = ""
while op != "no":
    def buscar(n:int,lista):
        izq = 0
        der = len(lista)-1
        encontrado = False
        n = int(input("Numero del Array: "))
        while encontrado == False and izq <= der:

            cen = (izq + der)//2

            if lista[cen] == n:
                encontrado = True

            elif lista[cen] < n:
                izq = cen+1 # para descartar la posición del centro y la parte izquierda, luego rodarlo una posicion +
            
            else:
                der = cen-1 # para descartar la posición del centro y la parte derecha, luego rodarlo una posicion -

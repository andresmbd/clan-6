print("\nEjercicio #11: Factura Heladeria\n")

decision = True
contador = 0
acumulador = 0
cono = 0
vaso = 0
banana_split = 0
total = 0

while decision:
    
    producto = input("1. cono\n2. vaso\n3. banana split\nIngrese el producto o numero: ").lower()
    cantidad = int(input("Cantidad: "))
    
    if producto == "cono" or producto == "1":
        cono += cantidad
        total = 3000 * cantidad      
    elif producto == "vaso" or producto == "2":
        vaso += cantidad
        total = 4000 * cantidad      
    elif producto == "banana split" or producto == "3":
        banana_split += cantidad
        total = 9000 * cantidad
    else: 
        print("Ingrese el producto correcto")
        continue
        

    contador += 1
    acumulador += total
    
    continuar = input("Continuar:\n1. Si\n2. No\n-> ").lower()

    if continuar == "si" or continuar == "1":
        decision = True
    elif continuar == "no" or continuar == "2":
        decision = False
        print("Total Vendido: \n$", acumulador, "\nNumero de clientes: \n", contador, "\nProducto mas vendido:")
        if cono > vaso and cono > banana_split:
            print("Cono: ", cono)
        elif vaso > cono and vaso > banana_split:
            print("Vaso: ", vaso)
        elif banana_split > cono and banana_split > vaso:
            print("Banana split: ", banana_split)
        # elif cono == vaso or banana_split # or vaso == cono or banana_split or banana_split == cono and vaso:



    

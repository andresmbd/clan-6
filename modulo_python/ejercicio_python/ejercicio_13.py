print("\nEjercicio #13: Cafetería\n")

decision_usuario = True
cafe = 4000
capuchino = 7000
pastel = 6000
acumulador = 0
acumulador_descuento = 0
venta = 0

while decision_usuario:

    print("\nCafetería: descuento por consumo" \
            "\n1. Cafe"\
                "\n2. Capuchino"\
                    "\n3. Pastel")
    continuar_pedir =  True
    while continuar_pedir:

        entrada = input("Que pedido va a llevar: ").lower()

        if entrada == "cafe" or entrada == "1":
            venta += cafe 

        elif entrada == "capuchino" or entrada == "2":
            venta += capuchino

        elif entrada == "pastel" or entrada == "3":
            venta += pastel

        continuar = input("Continuar pidiendo? (si o no): ")
        if continuar == "si":
            continuar_pedir == True
        elif continuar == "no":
            continuar_pedir = False
            total_cliente = venta
            print("Subtotal: $", total_cliente)           
            if total_cliente > 20000:
                descuento = (total_cliente - (total_cliente * .10)) 
                print("\nAgregado 10% de descuento\nTotal: $", descuento)
                acumulador_descuento += descuento
            else:
                print("Total: $", total_cliente)
                acumulador += total_cliente

    venta = 0
        
    siguiente_cliente = input("\nSiguiente cliente (Sí o No): ").lower()
    if siguiente_cliente == "si":
        decision_usuario = True

    elif siguiente_cliente == "no":
        decision_usuario = False
        total_dia = acumulador + acumulador_descuento
        print("Total acumulado del dia: $", total_dia)





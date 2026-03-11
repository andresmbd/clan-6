print("\nEjercicio #3: Cafeteria\n")

cafe = 4000
te = 3500
jugo = 5000

entrada_bebida = input("Qué bebida quieres: ").lower()
entrada_cantidad = int(input("Cuantas unidades deseas comprar: "))

if entrada_bebida == "cafe":
    total_compra = cafe * entrada_cantidad 
    print("Total a pagar: $", total_compra)

elif entrada_bebida == "te":
    total_compra = te * entrada_cantidad 
    print("Total a pagar: $", total_compra)

elif entrada_bebida == "jugo":
    total_compra = jugo * entrada_cantidad 
    print("Total a pagar: $", total_compra)

else:
    print("OPCION INVALIDA INTENTALO OTRA VEZ")
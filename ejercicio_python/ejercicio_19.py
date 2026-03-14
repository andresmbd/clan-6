print("\nEjercicio #19: Tienda de ropa deportiva\n")
agotado = 0
stock_bajo = 0
stock_normal = 0
for i in range(1, 11, 1):
    producto = input("\nNombre producto: ")
    cantidad_dispo = int(input("Cantidad disponible: "))

    if cantidad_dispo == 0:
        agotado += 1
    elif cantidad_dispo >= 1 and cantidad_dispo <= 5:
        stock_bajo += 1
    elif cantidad_dispo > 5:
        stock_normal += 1
print("Agotados: ", agotado)
print("Stock bajo: ", stock_bajo)
print("Stock normal: ", stock_normal)

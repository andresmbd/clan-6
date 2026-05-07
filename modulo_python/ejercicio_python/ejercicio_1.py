print("\nEjercicio #1: Heladeria\n")


vainilla = 0
chocolate = 0
fresa = 0

for i in range(1,6,1):
    print("1. Vainilla\n2. Chocolate\n3. Fresa")
    selecciona_sabor = input("Elige tu sabor: ").lower()
    if selecciona_sabor == "vainilla" or selecciona_sabor == "1":
        vainilla += 1
    elif selecciona_sabor == "chocolate" or selecciona_sabor == "2":
        chocolate += 1
    elif selecciona_sabor == "fresa" or selecciona_sabor == "3":
        fresa += 1
print("\nCantidad de vainilla: ", vainilla, "\nCantidad de chocolate: ", chocolate, "\nCantidad de fresa: ", fresa)






print("\nEjercicio #8: Tienda deportiva\n")

contador = 0
for i in range(1,7,1):
    precio_producto = int(input("Ingrese el precio: "))
    if precio_producto > 100000:
        contador += 1
print(contador, "productos cuestan más de $100000")

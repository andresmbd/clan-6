print("\nEjercicio #16: Tienda de mascotas:\n")

alimento = 0
juguete = 0
accesorio = 0

for i in range(1, 11, 1):
    categoria = input("Categoria de la compra: ").lower()
    valor = float(input("Valor de la compra: "))

    if categoria == "alimento":
        alimento += valor

    elif categoria == "juguete":
        juguete += valor

    elif categoria == "accesorio":
        accesorio += valor

print("\nInforme de venta por categoria\nAlimento: $", alimento, "\nJuguete: $", juguete, "\nAccesorio: $", accesorio)

print("Categoría generó más dinero:")
if alimento > juguete and alimento > accesorio:
    print("Categoria Alimento ")
elif juguete > alimento and juguete > accesorio:
    print("Categoria Juguete")
elif accesorio > juguete and accesorio > alimento:
    print("Categoria Accesorio")


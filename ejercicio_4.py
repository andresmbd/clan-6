print("\nEjercicio #4: Cine\n")

edad_cliente = int(input("Cuantos años tienes: "))
if edad_cliente < 12:
    print("La entrada cuesta $ 8000")

elif edad_cliente >= 12 and edad_cliente <= 59:
    print("La entrada cuesta $ 12000")

else:
    print("La entrada cuesta $ 9000")
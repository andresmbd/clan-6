print("\nEjercicio #2: Gimnasio\n")

edad_persona = int(input("Cual es tu edad: "))

if edad_persona < 13:
    print("No puedes ingresar")
elif edad_persona >= 13 and edad_persona <= 17:
    print("Tienes clase juvenil")

elif edad_persona >= 18 and edad_persona <= 59:
    print("Tienes clase general")
else:
    print("Clase senior")



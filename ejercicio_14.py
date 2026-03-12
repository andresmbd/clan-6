print("\nEjercicio #14: Cine\n")


capacidad_total = int(input("Capacidad total de sala de cine: "))
ingreso_persona = int(input("Cuantas personas ingresaron: "))
niño = 0
adulto = 0
adulto_mayor = 0

for i in range(1, ingreso_persona + 1, 1):
    edad = int(input("Cuantos años tienes: "))
    if edad < 12:
        niño += 1
    elif edad >= 30 and edad <= 59:
        adulto += 1
    elif edad > 60:
        adulto_mayor += 1


print("Total de personas ingresadas: ", ingreso_persona,"\nCantidad de niños: ", niño, "cantidad de adultos: ", adulto, "Cantidad de adultos mayores: ", adulto_mayor)

if capacidad_total == ingreso_persona:
    print("La sala esta llena")

elif capacidad_total > ingreso_persona:
    print("La sala no esta llena")




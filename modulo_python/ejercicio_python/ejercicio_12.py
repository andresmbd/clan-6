print("\nEjercicio #12: Gimnacio\n")


contador_bajo = 0
contador_medio = 0
contador_alto = 0

for i in range(1,6,1):

    nombre = input("Nombre: ")
    dias_asistidos = int(input("Que dias asististe en la semana: "))
    minutos_promedio = int(input("Minuto promedio entrenado por dia: "))

    if dias_asistidos < 3:
        # print("Bajo compromiso")
        contador_bajo += 1

    elif dias_asistidos >= 3 and dias_asistidos <= 4:
        # print("Compromiso medio")
        contador_medio += 1
    else:
        # print("Compromiso alto")
        contador_alto += 1

print("Personas con compromiso bajo: ", contador_bajo,"\nPersonas con compromiso medio: ", contador_medio,"\nPersonas con compromiso alto: ", contador_alto)
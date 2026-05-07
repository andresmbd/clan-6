print("\nEjercicio #18: Centro de idiomas\n")
num_estudiante = int(input("Numero de estudiantes del grupo: "))
bajo = 0
medio = 0
alto = 0
mejor_estudiante = ""
prom_alto = 0
acumulador_prom = 0

for i in range(1, num_estudiante + 1, 1):
    nombre = input("Nombre del estudiante: ")
    speaking = int(input("Nota speaking: "))
    listening = int(input("Nota listening: "))
    reading = int(input("Nota reading: "))

    promedio = (speaking + listening + reading) / 3

    if promedio < 60:
        bajo += 1
        acumulador_prom += promedio

    elif promedio >=60 and promedio <= 79:
        medio += 1
        acumulador_prom += promedio
    elif promedio >= 80:
        alto += 1
        acumulador_prom += promedio

    if promedio > prom_alto:
        prom_alto = promedio
        mejor_estudiante = nombre

promedio_general = acumulador_prom / num_estudiante

print(f"Promedio general del grupo:  {promedio_general:.1f}")
print(f"Mejor estudiante: {mejor_estudiante} Promedio mayor: {prom_alto:.1f}")
print(f"Division de Promedio:\nBajo {bajo}\nMedio {medio}\nAlto {alto}")
    
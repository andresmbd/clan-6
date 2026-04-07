print("\nEjercicio #7: Peluqueria\n")

hora_llegada = int(input("Hora de llegada en formato entero (0-23): "))

if hora_llegada >= 6 and hora_llegada <= 11:
    print("Rango del dia: mañana")
elif hora_llegada >= 12 and hora_llegada <= 17:
    print("Rango del dia: tarde")
elif hora_llegada >= 18 and hora_llegada <= 22:
    print("Rango del dia: noche")
else:
    print("Fuera de horario")



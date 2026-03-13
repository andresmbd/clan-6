print("\nEjercicio #10: Academia de baile\n")

asistencia = int(input("Cantidad de asistencia a la academia: "))

if asistencia < 5:
    print("Asistencia baja ")
elif asistencia >= 5 and asistencia <= 8:
    print("Asistencia media")
else:
    print("Asistencia alta")
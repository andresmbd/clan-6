print("\nEjercicio #6: Parqueadero\n")


horas_parqueda = int(input("Horas parqueadas del carro: "))
primera_hora = 5000

if horas_parqueda > 1:
    total_pagar = (3000 * (horas_parqueda - 1)) + primera_hora

else:
    total_pagar = primera_hora

print("Total a pagar: $", total_pagar)
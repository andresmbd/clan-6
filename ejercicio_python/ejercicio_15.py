print("\nEjercicio #15: Parqueadero\n")
recaudo_carro = 0
recaudo_moto = 0
carro = 0
moto = 0
pago_mayor = 0
placa_pago_mayor = ""

for i in range(1, 9, 1):
    placa = input("Ingresar placa: ")
    tipo_vehiculo = input("Ingresar el tipo de vehiculo: ").lower()
    horas_parqueado = int(input("Horas parqueado: "))


    if tipo_vehiculo == "carro":
        pago = 4000 * horas_parqueado
        carro += 1
        recaudo_carro += pago

    elif tipo_vehiculo == "moto":
        pago = 2000 * horas_parqueado
        moto += 1
        recaudo_moto += pago
    
    recaudo_total = recaudo_carro + recaudo_moto

    if pago > pago_mayor:
        pago_mayor = pago
        placa_pago_mayor = placa

print("Total recaudado: ", recaudo_total)
print("Carros ingresados: ", carro)
print("Motos ingresados: ", moto)
print("Vehiculo con mayor pago: ", placa_pago_mayor, "Total pagado: ", pago_mayor)


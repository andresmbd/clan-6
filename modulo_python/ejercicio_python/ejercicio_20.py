print("\nEjercicio #20: Club recreativo\n")

contador_basico = 0
contador_premium = 0
contador_familiar = 0

acumulador_basico = 0
acumulador_premium = 0
acumulador_familiar = 0

num_personas = int(input("Numero de personas por ingresar: "))
for i in range(1, num_personas + 1, 1):
    nombre = input("\nNombre: ")
    edad = int(input("Edad: "))

    if edad < 18:
        print("Mostrar registro juvenil")
    elif edad >= 60:
        print("Mostrar beneficio senior")

    plan = input("Tipo de plan (1. basico 2. premium 3. familiar): ").lower()

    if plan == "basico" or plan == "1":
        acumulador_basico += 50000
        contador_basico += 1
    elif plan == "premium" or plan == "2":
        acumulador_premium += 90000
        contador_premium += 1
    elif plan == "familiar" or plan == "3":
        acumulador_familiar += 130000
        contador_familiar += 1

recaudo_total = acumulador_basico + acumulador_premium + acumulador_familiar
    
print(f"\nTotal recaudado: $ {recaudo_total}\nCantidad de personas por plan:\nBasico: {contador_basico} | Premium: {contador_premium} | Familiar: {contador_familiar}")
print("Plan más vendido:")
if contador_basico > contador_premium and contador_basico > contador_familiar:
    print("Basico")
elif contador_familiar > contador_basico and contador_familiar > contador_premium:
    print("Familiar")
elif contador_premium > contador_basico and contador_premium > contador_familiar:
    print("Premium")
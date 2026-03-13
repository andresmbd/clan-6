print("\nEjercicio #17: Peluqueria:\n")
total_dia = 0
corte = 0
cepillado = 0
tintura = 0

for i in range(1, 8, 1):
    nombre = input("\nNombre del cliente: ")
    servicio_solicitado = input("Ingrese el servicio deseado (1. corte, 2. cepillado, 3. tintura): ").lower()
    valor_pagado = int(input("Valor a pagar: $ "))

    total_dia += valor_pagado
    if servicio_solicitado == "corte" or servicio_solicitado == "1":
        corte += 1

    elif servicio_solicitado == "cepillado" or servicio_solicitado == "2":
        cepillado += 1

    elif servicio_solicitado == "tintura" or servicio_solicitado == "3":
        tintura += 1
    
print(f"\nTotal del dia ${total_dia}\n Cantidad por servicio:\nCorte {corte} | Cepillado {cepillado} | Tintura {tintura}")
print("Servicio mas solicitado:")
if corte > cepillado and corte > tintura:
    print("Corte")
elif cepillado > corte and cepillado > tintura:
    print("Cepillado")
elif tintura > corte and tintura > cepillado:
    print("Tintura")




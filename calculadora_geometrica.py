print("CALCULADORA GEOMETRICA")

opcion = 0
# while opcion != 10:
print("Selecciona el numero o la figura para calcular\n"\
    "1. Rectangulo\n"\
    "2. Triangulo\n"\
    "3. Circulo\n"\
    "4. Trapecio\n"\
    "5. Esfera\n"\
    "6. Cilindro\n"\
    "7. Cono\n"\
    "8. Piramide\n"\
    "9. Triangulo Rectangulo\n"\
    "10. Salir")
entrada = input("-> ").lower()
if entrada == "rectangulo" or entrada == "1":
    operacion = input("Selecciona la operacion:\n"\
                    "1. Area\n"\
                    "2. Perimetro\n"\
                    "3. Diagonal\n"\
                    "-> ").lower()
    
    if operacion == "area" or operacion == "1":
        entrada = input("Selecciona la variable a averiguar\n"\
                    "1. Base\n"\
                    "2. Altura\n"\
                    "3. Area\n"\
                    "-> ").lower()
        
        if entrada == "base" or entrada == "1":
            a = float(input("Ingrese el valor de area (float): "))
            h = float (input("Ingrese el valor de altura (float): "))
            b = a / h
            print(f"Resultado {b:.1f}")

        elif entrada == "altura" or entrada == "2":
            b = float(input("Ingrese el valor de base (float): "))
            a = float(input("Ingrese el valor de area (float): "))
            h = a / b
            print(f"Resultado {h:.1f}")

        elif entrada == "area" or entrada == "3":
            b = float(input("Ingrese el valor de base (float): "))
            h = float (input("Ingrese el valor de altura (float): "))
            a = b * h           
            print(f"Resultado {a:.1f}")

    elif operacion == "perimetro" or operacion == "2":
        entrada = input("Selecciona la variable a averiguar\n"\
                    "1. Perimetro\n"\
                    "2. Base\n"\
                    "3. Altura\n"\
                    "-> ")
        b = float(input("Ingrese el valor de base (float): "))
        h = float(input("Ingrese el valor de altura (float): "))
        p = 2 * (b + h)
        print(f"Resultado {p:.1f}")
    # elif operacion == "diagonal" or operacion == "3":
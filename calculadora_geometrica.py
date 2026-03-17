print("\nCALCULADORA GEOMETRICA")
print("\nLa Calculadora Geometrica maneja la unidad de longitud Pulgada (in)")
variable = ""
entrada = ""
while entrada != "10":
    print("\nSelecciona el numero o la figura para calcular\n"\
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
    # operaciones del rectangulo
    if entrada == "rectangulo" or entrada == "1":
        operacion = input("Selecciona la operacion:\n"\
                        "1. Area\n"\
                        "2. Perimetro\n"\
                        "3. Diagonal\n"\
                        "-> ").lower()
        
        if operacion == "area" or operacion == "1":
            variable = input("Selecciona la variable a averiguar\n"\
                        "1. Base\n"\
                        "2. Altura\n"\
                        "3. Area\n"\
                        "-> ").lower()
            
            # operacion area
            if variable == "base" or variable == "1": # si se quiere calcular la base 
               
                a = float(input("Ingrese el valor del area (float): "))
                h = float (input("Ingrese el valor de la altura (float): "))
                if a > 0 and h > 0:
                    b = a / h
                    print(f"Resultado Base = {b:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")
                    
                    
            elif variable == "altura" or variable == "2": # si se quiere calcular la altura
                b = float(input("Ingrese el valor de la base (float): "))
                a = float(input("Ingrese el valor del area (float): "))
                if b > 0 and a > 0:
                    h = a / b
                    print(f"Resultado Altura = {h:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "area" or variable == "3": # si se quiere calcular el area
                b = float(input("Ingrese el valor de la base (float): "))
                h = float (input("Ingrese el valor de la altura (float): "))
                if b > 0 and h > 0:
                    a = b * h           
                    print(f"Resultado Area = {a:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")
        
           
        # operacion perimetro
        elif operacion == "perimetro" or operacion == "2":
            variable = input("Selecciona la variable a averiguar\n"\
                        "1. Perimetro\n"\
                        "2. Base\n"\
                        "3. Altura\n"\
                        "-> ").lower()
            if variable == "perimetro" or variable == "1": 
                b = float(input("Ingrese el valor de la base (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if b > 0 and h > 0:
                    p = 2 * (b + h)
                    print(f"Resultado Perimetro = {p:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "base" or variable == "2":
                p = float(input("Ingrese el valor del perimetro (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if p > 0 and h > 0:
                    b = (p - (2 * h)) / 2
                    print(f"Resultado Base = {b:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "altura" or variable == "3":
                p = float(input("Ingrese el valor del perimetro (float): "))
                b = float(input("Ingrese el valor de la base (float): "))
                if p > 0 and b > 0:
                    h = (p - (2 * b)) / 2
                    print(f"Resultado Altura {h:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

        # operaacion diagonal
        elif operacion == "diagonal" or operacion == "3":
            variable = input("Selecciona la variable a averiguar\n"\
                        "1. Diagonal\n"\
                        "2. Base\n"\
                        "3. Altura\n"\
                        "-> ").lower()
            if variable == "diagonal" or variable == "1":
                b = float(input("Ingrese el valor de la base (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if b > 0 and h > 0:
                    d = ((b ** 2) + (h ** 2)) ** (1 / 2)
                    print(f"Resultado Diagonal = {d:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
            
            elif variable == "base" or variable == "2":
                d = float(input("Ingrese el valor de la diagonal (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if d > 0 and h > 0:
                    b = ((d ** 2) - (h ** 2)) ** (1 / 2)
                    print(f"Resultado Base = {b:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
            
            elif variable == "altura" or variable == "3":
                d = float(input("Ingrese el valor de la diagonal (float): "))
                b = float(input("Ingrese el valor de la base (float): "))
                if d > 0 and b > 0:
                    h = ((d ** 2) - (b ** 2)) ** (1/2)
                    print(f"Resultado Altura = {h:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

    # operaciones del triangulo
    elif entrada == "triangulo" or entrada == "2":
        operacion = input("Selecciona la operacion:\n"\
                        "1. Area\n"\
                        "2. Perimetro\n" \
                        "3. Angulos\n"\
                        "-> ").lower()
        if operacion == "area" or operacion == "1":
            variable = input("Selecciona la variable a averiguar\n"\
                        "1. Area\n"\
                        "2. Base\n"\
                        "3. Altura\n"\
                        "-> ").lower()
            if variable == "area" or variable == "1":
                b = float(input("Ingrese el valor de la base (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if b > 0 and h > 0:
                    a = (b * h) / 2
                    print(f"Resultado Area = {a:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "base" or variable == "2":
                a = float(input("Ingrese el valor del area (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if a > 0 and h > 0:
                    b = (2 * a) / h
                    print(f"Resultado Base = {b:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "altura" or variable == "3":
                a = float(input("Ingrese el valor del area (float): "))
                b = float(input("Ingrese el valor de la base (float): "))
                if a > 0 and b > 0:
                    h = (2 * a) / b
                    print(f"Resultado Altura = {h:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

        elif operacion == "perimetro" or operacion == "2":
            variable = input("Selecciona la variable a averiguar\n"\
                        "1. Perimetro\n"\
                        "2. Lado a\n"\
                        "3. Lado b\n"\
                        "4. Lado c\n"\
                        "-> ").lower()
            if variable == "perimetro" or variable == "1":
                a = float(input("Ingrese el valor del lado a (float): "))
                b = float(input("Ingrese el valor del lado b (float): "))
                c = float(input("Ingrese el valor del lado c (float): "))
                if a > 0 and b > 0 and c > 0:
                    p = a + b + c
                    print(f"Resultado Perimetro = {p:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "lado a" or variable == "2":
                b = float(input("Ingrese el valor del lado b (float): "))
                c = float(input("Ingrese el valor del lado c (float): "))
                p = float(input("Ingrese el valor del perimetro (float): "))
                if b > 0 and c > 0 and p > 0:
                    a = p - b - c
                    print(f"Resultado Lado a = {a:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "lado b" or variable == "3":
                a = float(input("Ingrese el valor del lado a (float): "))
                c = float(input("Ingrese el valor del lado c (float): "))
                p = float(input("Ingrese el valor del perimetro (float): "))
                if a > 0 and c > 0 and p > 0:
                    b = p - a - c
                    print(f"Resultado Lado b = {b:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "lado c" or variable == "4":
                a = float(input("Ingrese el valor del lado a (float): "))
                b = float(input("Ingrese el valor del lado b (float): "))
                p = float(input("Ingrese el valor del perimetro (float): "))
                if a > 0 and b > 0 and p > 0:
                    c = p - a - b
                    print(f"Resultado Lado c = {c:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

        elif operacion == "angulos" or operacion == "3":
            variable = input("Selecciona el angulo a averiguar\n" \
                        "1. A\n" \
                        "2. B\n" \
                        "3. C\n" \
                        "-> ").lower()
            if variable == "a" or variable == "1":
                b = float(input("Ingrese el valor del angulo b (float): "))
                c = float(input("Ingrese el valor del angulo c (float): "))
                a = 180 - (b + c)
                if a > 0 and a < 180:
                    print(f"Resultado Angulo a = {a:.2f}°")
                else:
                    print("\nValor incorrecto en el mundo real")
            
            elif variable == "b" or variable == "2":
                a = float(input("Ingrese el valor del angulo a (float): "))
                c = float(input("Ingrese el valor del angulo c (float): "))
                b = 180 - (a + c)
                if b > 0 and b < 180:
                    print(f"Resultado Angulo b = {b:.2f}°")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "c" or variable == "3":
                a = float(input("Ingrese el valor del angulo a (float): "))
                b = float(input("Ingrese el valor del angulo b (float): "))
                c = 180 - (a + b)
                if c > 0 and c < 180:
                    print(f"Resultado Angulo c = {c:.2f}°")
                else:
                    print("\nValor incorrecto en el mundo real")

    # operaciones del circulo
    elif entrada == "circulo" or entrada == "3":
        operacion = input("Selecciona la operacion:\n"\
                        "1. Area\n"\
                        "2. Circunferencia\n" \
                        "3. Radio\n" \
                        "-> ").lower()
        
        if operacion == "area" or operacion == "1":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Area\n" \
                        "2. Radio\n" \
                        "-> ").lower()
            if variable == "area" or variable == "1":
                r = float(input("Ingrese el valor del radio (float): "))
                if r > 0:
                    a = 3.14 * (r ** 2)
                    print(f"Resultado Area = {a:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "radio" or variable == "2":
                a = float(input("Ingrese el valor del area (float): "))
                if a > 0:
                    r = (a / 3.14) ** (1 / 2)
                    print(f"Resultado Radio = {r:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
               
        elif operacion == "circunferencia" or operacion == "2":
            variable = input("Selecciona la variable a averiguar\n"
                        "1. Circunferencia\n"
                        "2. Radio\n"
                        "3. Diametro\n"
                        "-> ").lower()

            if variable == "circunferencia" or variable == "1":
                r = float(input("Ingrese el valor del radio (float): "))
                if r > 0:
                    c = 2 * 3.14 * r
                    print(f"Resultado Circunferencia = {c:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
               
            elif variable == "radio" or variable == "2":
                c = float(input("Ingrese el valor de la circunferencia (float): "))
                if c > 0:
                    r = c / (2 * 3.14)
                    print(f"Resultado Radio = {r:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "diametro" or variable == "3":
                c = float(input("Ingrese el valor de la circunferencia (float): "))
                if c > 0:
                    d = c / 3.14
                    print(f"Resultado Diametro = {d:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

        elif operacion == "radio" or operacion == "3":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Radio\n" \
                        "2. Diametro\n" \
                        "-> ").lower()
            if variable == "radio" or variable == "1":
                d = float(input("Ingrese el valor del diametro (float): "))
                if d > 0:
                    r = d / 2
                    print(f"Resultado Radio = {r:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
            
            elif variable == "diametro" or variable == "2":
                r = float(input("Ingrese el valor del radio (float): "))
                if r > 0:
                    d = r * 2
                    print(f"Resultado Radio = {d:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

    # operaciones del trapecio
    elif entrada == "trapecio" or entrada == "4":
        operacion = input("Selecciona la operacion:\n" \
                    "1. Area\n" \
                    "2. Perimetro\n" \
                    "-> ").lower()
        if operacion == "area" or operacion == "1":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Base mayor\n" \
                        "2. Base menor\n" \
                        "3. Altura\n" \
                        "4. Area\n" \
                        "-> ").lower()
            if variable == "base mayor" or variable == "1":
                a = float(input("Ingrese el valor del area (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                b_menor = float(input("Ingrese el valor de la base menor (float): "))
                if a > 0 and h > 0 and b_menor > 0:
                    b_mayor = ((2 * a) / h) - b_menor
                    print(f"Resultado Base mayor = {b_mayor:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "base menor" or variable == "2":
                a = float(input("Ingrese el valor del area (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                b_mayor = float(input("Ingrese el valor de la base mayor (float): "))
                if a > 0 and h > 0 and b_mayor > 0:
                    b_menor =((2 * a) / h) - b_mayor
                    print(f"Resultado Base menor = {b_menor:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "altura" or variable == "3":
                b_mayor = float(input("Ingrese el valor de la base mayor (float): "))
                b_menor = float(input("Ingrese el valor de la base menor (float): "))
                a = float(input("Ingrese el valor del area (float): "))
                if b_mayor > 0 and b_menor > 0 and a > 0:
                    h = (2 * a) / (b_mayor + b_menor)
                    print(f"Resultado Altura = {h:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "area" or variable == "4":
                b_mayor = float(input("Ingrese el valor de la base mayor (float): "))
                b_menor = float(input("Ingrese el valor de la base menor (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if h > 0 and b_menor > 0 and b_mayor > 0:
                    a = ((b_mayor + b_menor) * h ) / 2
                    print(f"Resultado Area = {a:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")

        if operacion == "perimetro" or operacion == "2":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Perimetro\n" \
                        "2. Base mayor\n" \
                        "3. Base menor\n" \
                        "4. Lado 1\n" \
                        "5. Lado 2\n" \
                        "-> ").lower()
            if variable == "perimetro" or variable == "1":
                b_mayor = float(input("Ingrese el valor de la base mayor (float): "))
                b_menor = float(input("Ingrese el valor de la base menor (float): "))
                lado_1 = float(input("Ingrese el valor del lado 1 (float):  "))
                lado_2 = float(input("Ingrese el valor del lado 2 (float):  "))
                if b_mayor > 0 and b_menor > 0 and lado_1 > 0 and lado_2 > 0:
                    p = b_mayor + b_menor + lado_1 + lado_2
                    print(f"Resultado Perimetro = {p:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "base mayor" or variable == "2":
                b_menor = float(input("Ingrese el valor de la base menor (float): "))
                lado_1 = float(input("Ingrese el valor del lado 1 (float):  "))
                lado_2 = float(input("Ingrese el valor del lado 2 (float):  "))
                p = float(input("Ingrese el valor del perimetro (float):  "))
                if b_menor > 0 and lado_1 > 0 and lado_2 > 0 and p > 0:
                    b_mayor = p - (b_menor + lado_1 + lado_2)
                    print (f"Resultado Base mayor = {b_mayor:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "base menor" or variable == "3":
                b_mayor = float(input("Ingrese el valor de la base mayor (float): "))
                lado_1 = float(input("Ingrese el valor del lado 1 (float):  "))
                lado_2 = float(input("Ingrese el valor del lado 2 (float):  "))
                p = float(input("Ingrese el valor del perimetro (float):  "))
                if b_mayor > 0 and lado_1 > 0 and lado_2 and p > 0:
                    b_menor = p - (b_mayor + lado_1 + lado_2) 
                    print(f"Resultado Base menor = {b_menor:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
            
            elif variable == "lado 1" or variable == "4":
                lado_2 = float(input("Ingrese el valor del lado 2 (float):  "))
                b_mayor = float(input("Ingrese el valor de la base mayor (float): "))
                b_menor = float(input("Ingrese el valor de la base menor (float): "))
                p = float(input("Ingrese el valor del perimetro (float):  "))
                if lado_2 > 0 and b_mayor > 0 and b_menor > 0 and p > 0:
                    lado_1 = p - (lado_2 + b_mayor + b_menor)
                    print(f"Resultado Lado 1 = {lado_1:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "lado 2" or variable == "5":
                b_mayor = float(input("Ingrese el valor de la base mayor (float): "))
                b_menor = float(input("Ingrese el valor de la base menor (float): "))
                lado_1 = float(input("Ingrese el valor del lado 1 (float):  "))
                p = float(input("Ingrese el valor del perimetro (float):  "))
                if b_mayor > 0 and b_menor > 0 and lado_1 > 0 and p > 0: 
                    lado_2 = p - (lado_1 + b_mayor + b_menor)
                    print(f"Resultado Lado 2 = {lado_2:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
    # operaciones de la esfera
    elif entrada == "esfera" or entrada == "5":
        operacion = input("Selecciona la operacion:\n" \
                    "1. Volumen\n" \
                    "2. Area superficial\n" \
                    "-> ").lower()
        if operacion == "volumen" or operacion == "1":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Volumen\n" \
                        "2. Radio\n" \
                        "-> ").lower()
            if variable == "volumen" or variable == "1":
                r = float(input("Ingrese el valor del radio (float): "))
                if r > 0:
                    v = (4 / 3) * (3.14 * (r ** 3))
                    print(f"Resultado Volumen = {v:.2f} in^3")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "radio" or variable == "2":
                v = float(input("Ingrese el valor del volumen (float): "))
                if v > 0:
                    r = ((3 * v) / (4 * 3.14)) ** (1 / 3)
                    print(f"Resultado Radio = {r:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
        
        elif operacion == "area superficial" or operacion == "2":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Area\n" \
                        "2. Radio\n" \
                        "-> ").lower()          
            if variable == "area" or variable == "1":
                r = float(input("Ingrese el valor del radio (float): "))
                if r > 0:
                    a = 4 * 3.14 * (r ** 2)
                    print(f"Resultado Area superficial = {a:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "radio" or variable == "2":
                a = float(input("Ingrese el valor del area superficial (float): "))
                if a > 0:
                    r = (a / (4 * 3.14)) ** (1 / 2)
                    print(f"Resultado Radio = {r:.2f} in")    

    # operaciones del cilindro
    elif entrada == "cilindro" or entrada == "6":
        operacion = input("Selecciona la operacion:\n" \
                    "1. Volumen\n" \
                    "2. Area lateral\n" \
                    "3. Area total\n" \
                    "-> ").lower()
        if operacion == "volumen" or operacion == "1":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Volumen\n" \
                        "2. Radio de base\n" \
                        "3. Altura\n" \
                        "-> ").lower()
            if variable == "volumen" or variable == "1":
                r = float(input("Ingrese el valor del radio (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if r > 0 and h > 0:
                    v = 3.14 * (r ** 2) * h
                    print(f"Resultado Volumen = {v:.2f} in^3")
                else:
                    print("\nValor incorrecto en el mundo real")
            
            elif variable == "radio de base" or variable == "2":
                v = float(input("Ingrese el valor del volumen (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if v > 0 and h > 0:
                    r = (v / (3.14 * h)) ** (1 / 2)
                    print (f"Resultado Radio = {r:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "altura" or variable == "3":
                v = float(input("Ingrese el valor del volumen (float): "))
                r = float(input("Ingrese el valor del radio (float): "))
                if v > 0 and r > 0:
                    h = v / (3.14 * (r ** 2))
                    print(f"Resultado Altura = {h:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
        
        elif operacion == "area lateral" or operacion == "2":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Area lateral\n" \
                        "2. Radio\n" \
                        "3. Altura\n" \
                        "-> ").lower()
            if variable == "area lateral" or variable == "1":
                r = float(input("Ingrese el valor del radio (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if r > 0 and h > 0:
                    a_lateral = (2 * 3.14) * r * h
                    print(f"Resultado Area lateral = {a_lateral:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "radio" or variable == "2":
                a_lateral = float(input("Ingrese el valor del area lateral (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if a_lateral > 0 and h > 0:
                    r = a_lateral / (2 * 3.14 * h)
                    print(f" Resultado Radio = {r:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "altura" or variable == "3":
                a_lateral = float(input("Ingrese el valor del area lateral (float): "))
                r = float(input("Ingrese el valor del radio (float): "))
                if a_lateral > 0 and r > 0:
                    h = a_lateral / (2 * 3.14 * r)
                    print(f"Resultado Altura = {h:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
        
        elif operacion == "area total" or operacion == "3":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Area total\n" \
                        "2. Radio\n" \
                        "3. Altura\n" \
                        "-> ").lower()
            if variable == "area total" or variable == "1":
                r = float(input("Ingrese el valor del radio (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if r > 0 and h > 0:
                    a_total = (2 * 3.14) * r * (h + r)
                    print(f"Resultado Area total = {a_total:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "radio" or variable == "2":
                a_total = float(input("Ingrese el valor del area total (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if a_total > 0 and h > 0:
                    r = ((- 2 * 3.14 * h) + ((2 * 3.14 * h) ** 2 + (8 * 3.14 * a_total)) ** (1 / 2)) / (4 * 3.14)
                    print(f"Resultado Radio = {r:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
            
            elif variable == "altura" or variable == "3":
                a_total = float(input("Ingrese el valor del area total (float): "))
                r = float(input("Ingrese el valor del radio (float): "))
                if a_total > 0 and r > 0:
                    h = (a_total / (2 * 3.14 * r) ) - r
                    print(f"Resultado Altura = {h:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
    # operaciones del cono
    elif entrada == "cono" or entrada == "7":
        operacion = input("Selecciona la operacion:\n" \
                        "1. Volumen\n" \
                        "2. Area lateral\n" \
                        "3. Area Total\n" \
                        "-> ").lower()
        if operacion == "volumen" or operacion == "1":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Volumen\n" \
                        "2. Radio\n" \
                        "3. Altura\n" \
                        "-> ").lower()
            if variable == "volumen" or variable == "1":
                r = float(input("Ingrese el valor del radio (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if r > 0 and h > 0:
                    v = (1 / 3) * 3.14 * (r ** 2) * h
                    print(f"Resultado Volumen = {v:.2f} in^3")
                else:
                    print("\nValor incorrecto en el mundo real")
            
            elif variable == "radio" or variable == "2":
                v = float(input("Ingrese el valor del volumen (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if v > 0 and h > 0:
                    r = ((3 * v) / (3.14 * h)) ** (1 / 2)
                    print(f"Resultado Radio = {r:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
            
            elif variable == "altura" or variable == "3":
                v = float(input("Ingrese el valor del volumen (float): "))
                r = float(input("Ingrese el valor del radio (float): "))
                if v > 0 and r > 0:
                    h = (3 * v) / (3.14 * (r ** 2))
                    print(f"Resultado Altura = {h:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
        
        elif operacion == "area lateral" or operacion == "2":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Area lateral\n" \
                        "2. Radio\n" \
                        "3. Generatriz (lado inclinado del cono)\n" \
                        "-> ").lower()
            if variable == "area lateral" or variable == "1":
                r = float(input("Ingrese el valor del radio (float): "))
                g = float(input("Ingrese el valor de la generatriz (float): "))
                if r > 0 and g > 0:
                    a_lateral = 3.14 * r * g
                    print(f"Resultado Area lateral = {a_lateral:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "radio" or variable == "2":
                a_lateral = float(input("Ingrese el valor del area lateral (float): "))
                g = float(input("Ingrese el valor de la generatriz (float): "))
                if a_lateral > 0 and g > 0:
                    r = a_lateral / (3.14 * g)
                    print(f" Resultado Radio = {r:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "generatriz" or variable == "3":
                a_lateral = float(input("Ingrese el valor del area lateral (float): "))
                r = float(input("Ingrese el valor del radio (float): "))
                if a_lateral > 0 and r > 0:
                    g = a_lateral / (3.14 * r)
                    print(f"Resultado Generatriz = {g:.2f} in")

        elif operacion == "area total" or operacion == "3":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Area total\n" \
                        "2. Radio\n" \
                        "3. Generatriz (lado inclinado del cono)\n" \
                        "-> ").lower()
            if variable == "area total" or variable == "1":
                r = float(input("Ingrese el valor del radio (float): "))
                g = float(input("Ingrese el valor de la generatriz (float): "))
                if r > 0 and g > 0:
                    a_total = (r * 3.14) * (g + r)
                    print(f"Resultado Area total = {a_total:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "radio" or variable == "2":
                a_total = float(input("Ingrese el valor del area total (float): "))
                g = float(input("Ingrese el valor de la generatriz (float): "))
                if a_total > 0 and g > 0:
                    r = ((- 3.14 * g) + (((3.14 * g) ** 2) + 4 * 3.14 * a_total) ** (1 /2)) / (2 * 3.14)
                    print(f"Resultado Radio = {r:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "generatriz" or variable == "3":
                a_total = float(input("Ingrese el valor del area total (float): "))
                r = float(input("Ingrese el valor del radio (float): "))
                if a_total > 0 and r > 0:
                    g = (a_total - (3.14 * ( r ** 2))) / (3.14 * r)
                    print(f"Resultado Generatriz = {g:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
    # operaciones de la piramide
    elif entrada == "piramide" or entrada == "8":
        operacion = input("Selecciona la operacion:\n" \
                        "1. Volumen\n" \
                        "2. Area lateral\n" \
                        "3. Area Total\n" \
                        "-> ").lower()
        if operacion == "volumen" or operacion == "1":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Volumen\n" \
                        "2. Area base\n" \
                        "3. Altura\n" \
                        "-> ").lower()
            if variable == "volumen" or variable == "1":
                a_base = float(input("Ingrese el valor del area de la base (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if a_base > 0 and h > 0:
                    v = (a_base * h) / 3
                    print(f"Resultado Volumen = {v:.2f} in^3")
                else:
                    print("\nValor incorrecto en el mundo real")
            
            elif variable == "area base" or variable == "2":
                v = float(input("Ingrese el valor del volumen (float): "))
                h = float(input("Ingrese el valor de la altura (float): "))
                if v > 0 and h > 0:
                    a_base = (3 * v) / h
                    print(f"Resultado Area de la base = {a_base:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")
            
            elif variable == "altura" or variable == "3":
                v = float(input("Ingrese el valor del volumen (float): "))
                a_base = float(input("Ingrese el valor del area de la base (float): "))
                if v > 0 and a_base > 0:
                    h = (3 * v) / a_base
                    print(f"Resultado Altura = {h:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
        
        elif operacion == "area lateral" or operacion == "2":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Area lateral\n" \
                        "2. Perimetro base\n" \
                        "3. Apotema (altura inclinada de la cara)\n" \
                        "-> ").lower()
            if variable == "area lateral" or variable == "1":
                p = float(input("Ingrese el valor del perimetro de la base (float): "))
                a = float(input("Ingrese el valor del apotema (float): "))
                if p > 0 and a > 0:
                    a_lateral = (p * a) / 2
                    print(f"Resultado Area lateral = {a_lateral:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "perimetro base" or variable == "2":
                a_lateral = float(input("Ingrese el valor del area lateral (float): "))
                a = float(input("Ingrese el valor de la apotema (float): "))
                if a_lateral > 0 and a > 0:
                    p = (2 * a_lateral) / a
                    print(f" Resultado Perimetro de la base = {p:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "apotema" or variable == "3":
                a_lateral = float(input("Ingrese el valor del area lateral (float): "))
                p = float(input("Ingrese el valor del perimetro de la base (float): "))
                if a_lateral > 0 and p > 0:
                    a = (a_lateral * 2) / p
                    print(f"Resultado Apotema = {a:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")

        elif operacion == "area total" or operacion == "3":
            variable = input("Selecciona la variable a averiguar\n" \
                        "1. Area total\n" \
                        "2. Area base\n" \
                        "3. Area lateral\n" \
                        "-> ").lower()
            
            if variable == "area total" or variable == "1":
                a_base = float(input("Ingrese el valor del area de la base (float): "))
                a_lateral = float(input("Ingrese el valor del area lateral (float): "))
                if a_base > 0 and a_lateral > 0:
                    a_total = a_base + a_lateral
                    print(f"Resultado Area total = {a_total:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "area base" or variable == "2":
                a_total = float(input("Ingrese el valor del area total (float): "))
                a_lateral = float(input("Ingrese el valor del area lateral (float): "))
                if a_total > 0 and a_lateral > 0:
                    a_base = a_total - a_lateral
                    print(f"Resultado Radio = {a_base:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")

            elif variable == "area lateral" or variable == "3":
                a_total = float(input("Ingrese el valor del area total (float): "))
                a_base = float(input("Ingrese el valor del radio (float): "))
                if a_total > 0 and a_base > 0:
                    a_lateral = a_total - a_base
                    print(f"Resultado Altura = {a_lateral:.2f} in^2")
                else:
                    print("\nValor incorrecto en el mundo real")
    # teorema de pitagoras
    elif entrada == "triangulo rectangulo" or entrada == "9":
            variable = input("Selecciona la variable a averiguar\n"\
                        "1. Cateto a\n"\
                        "2. Cateto b\n"\
                        "3. Hipotenusa\n"\
                        "-> ").lower()
            if variable == "cateto a" or variable == "1":
                b = float(input("Ingrese el valor del cateto b (float): "))
                c = float(input("Ingrese el valor de la hipotenusa (float): "))
                if b > 0 and c > 0: 
                    a = ((c ** 2) - (b ** 2)) ** (1 / 2)
                    print(f"Resultado Cateto a = {a:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
            
            elif variable == "cateto b" or variable == "2":
                a = float(input("Ingrese el valor del cateto a (float): "))
                c = float(input("Ingrese el valor de la hipotenusa (float): "))
                if a > 0 and c > 0:
                    b = ((c ** 2) - (a ** 2)) ** (1 / 2)
                    print(f"Resultado Cateto b = {b:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
            
            elif variable == "hipotenusa" or variable == "3":
                a = float(input("Ingrese el valor del cateto a (float): "))
                b = float(input("Ingrese el valor del cateto b (float): "))
                if a > 0 and b > 0:
                    c = ((a ** 2) + (b ** 2)) ** (1/2)
                    print(f"Resultado Hipotenusa = {c:.2f} in")
                else:
                    print("\nValor incorrecto en el mundo real")
    # salir
    elif entrada == "salir" or entrada == "10":
            print("\nUn gusto ayudarte con la Calculadora Geometrica\n"\
                "\n¡Vuelve pronto!\n")
    # cualquier otra opcion
    else:
        print("\nElige un numero o una palabra\n")
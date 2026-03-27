

def crear (diccionario:dict): # se agrega un nuevo item 
    id_ = int(input("Digite el id: "))
    nombre = input("Digite un nombre: ").capitalize()
    apellido = input("Digite el apellido: ").capitalize()
    edad = int(input("Digite la edad: "))
    nivel_ingles = input("Digite el nivel de inglés: ").upper()
    nuevo = len(coders) + 1
    # Nuevo coder
    diccionario[nuevo] = {"id":id_,"nombre":nombre, "apellido": apellido,"edad": edad, "nvlIngles": nivel_ingles}
    return diccionario



def mostrar(diccionario:dict):
    for clave, valor in diccionario.items():
        print(clave,"|", valor)

def buscar(diccionario:dict):
    busqueda_id = int(input("Digite el id a encontrar: "))
    print("Buscando por numero de documento")
    encontrado = None

    for llave, valor in diccionario.items():
        if valor["id"] == busqueda_id:
            encontrado = valor 
            
    if encontrado:
        print(encontrado)
        print("Encontrado")
    else:
        print("No encontrado")


def eliminar(diccionario:dict):
    clave = int(input("ingrese la clave del dict a eliminar: "))
    diccionario.pop(clave, "No existe")   
    return diccionario

def actualizar(diccionario):
    tipos = { # guardar funciones para usarla despues
    "id": int,
    "nombre": str,
    "apellido": str,
    "edad": int,
    "nivel": str
}
    correcto = False
    while correcto == False:
        try:
            clave = int(input("Ingresa la Clave: "))
            correcto = True
        except:
            print("Ingresa un int")
    
    campo = input("Que quieres cambiar (Id/Nombre/Apellido/Edad/Nivel): ").lower()
    nuevo_valor = input("Nuevo valor: ")
    
    coder = diccionario.get(clave)

    if coder: # si la llave esta en el dict
        if campo in tipos: # si el valor de la llave coincide con tipos{}
            if tipos[campo] == int: # y si sí , entonces si es un int
                if nuevo_valor.isdigit(): # confirmame que el nuevo valor sea int como tipos[campo]
                    coder[campo] = int(nuevo_valor) # Usa la función que está en tipos[campo] = int(nuevo_valor) or str(nuevo_valor)
                else:
                    print("No es un int")
            else:
                coder[campo] = nuevo_valor.capitalize()
        else:
            print("Campo incorrecto")
    else: # si no
        print("No encontrado")
    
    return diccionario


coders = {
    1: {
        "id": 1048229292,
        "nombre": "Jander",
        "apellido": "Arguello",
        "edad": 30,
        "nvlIngles": "-A0"
    },
    2: {
        "id": 1048229296,
        "nombre": "Luisa",
        "apellido": "De la Rosa",
        "edad": 19,
        "nvlIngles": "C30"
    },
    3: {
        "id": 1048229297,
        "nombre": "Maria",
        "apellido": "Sanchez",
        "edad": 19,
        "nvlIngles": "C1"
    }
}   

op = ""
while op != "salir":
    op = input("Selecciona la accion a ejecutar al diccionario:\n" \
    "Crear\n" \
    "Mostrar\n" \
    "Buscar\n" \
    "Actualizar\n" \
    "Eliminar\n"
    "Salir\n" \
    "-> ").lower()

    if op == "crear":
        coders = crear(coders)

    elif op == "mostrar":
        mostrar(coders)

    elif op == "buscar":
        buscar(coders)

    elif op == "actualizar":
        coders = actualizar(coders)

    elif op == "eliminar":
        coders = eliminar(coders)

    elif op == "salir":
        op = "salir"

    else:
        print("Opcion invalida")





"""
for valor in diccionario.values(): .values() da directamente los valores
     if valor["id"] == busqueda_id:
        encontrado = valoro
        
        o con
        
for _, valor in diccionario.items(): que el _ representa ignorar la variable

"""

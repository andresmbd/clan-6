


# print(coders)

def crear (diccionario:dict): # se agrega un nuevo item 
    id_ = int(input("Digite el id: "))
    nombre = input("Digite un nombre: ").capitalize()
    apellido = input("Digite el apellido: ").capitalize()
    edad = int(input("Digite la edad: "))
    nivel_ingles = input("Digite el nivel de inglés: ").upper()
    nuevo = len(coders) + 1
    # Nuevo coder
    diccionario[nuevo] = {"id":id_,"nombre":nombre, "apellido": apellido,"edad": edad, "nvlIngles": nivel_ingles}
    print("\nimprimiendo luego de añadir\n")
    print(diccionario)
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


def eliminar():
    
    pass
    
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


    # for j, k in coders.items():
    #     if k["id"] == busqueda_id:
            





# print("Buscando el nombre de un coder especifico")

# print(coders[4])

# print("Buscando con el metodo get")

# 



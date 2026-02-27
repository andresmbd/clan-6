
usuario = "riwicoder"
contraseña = "Qwe.123*"
cod_verificacion = "123456"

print("ACCESO DE SEGURIDAD\n")

usuario_ingresado = input("Ingrese su usuario: ").lower()
contraseña_ingresada = input("Ingrese la contraseña: ")

if usuario == usuario_ingresado and contraseña == contraseña_ingresada:
    print("\nPor terminos de seguridad requerimos el codigo de seguridad\n")
    cod_verificacion_ingresado = input("Ingrese el codigo de verificacion: ")

    if cod_verificacion == cod_verificacion_ingresado:
        print("\nACCESO CONCEDIDO, Bienvenido\n")
    else:
        print("\nACCESO DENEGADO, Intentelo más tarde\n")
else:
    print("\nEl usuario y/o la contraseña es incorrecto\n")
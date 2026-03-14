print("\nEjercicio #5: Tienda de mascotas\n")

tipo_mascota = input("Cual es tu tipo de mascota (Perro, gato o Conejo): ").lower()

if tipo_mascota == "perro":
    print("\nTu perro debe alimentase de Pechuga de pollo cocida, pavo, pescado\nZanahorias (ideales como snack), calabaza (buena para la digestión), brócoli y espinacas.\nManzana (sin semillas), pera, plátano y melón.")
elif tipo_mascota == "gato":
    print("\nTu gato debe alimentarse de Pollo, pavo, res y cordero (siempre cocidos para evitar bacterias como Salmonella).\nSalmón, atún o sardinas cocidas; aportan Omega 3 beneficioso para su pelaje.\nZanahoria, calabaza, calabacín, brócoli, manzana (sin semillas) y arándanos.")
elif tipo_mascota =="conejo":
    print("\nTu conejo debe alimentarse de 80% Heno\n15% Vegetales Frescos\n5% Pellets")

else:
    print("\nINGRESA EL VALOR DEL CAMPO CORRECTO")
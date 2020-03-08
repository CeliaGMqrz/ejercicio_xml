# Programa principal

# Funciones
from funciones_clinicavet import *
# Definir el arbol
arbol = etree.parse('clinica_veterinaria.xml')

# MENU 

while True:
    print()
    print("___________________________CLINICAVET__________________________________")
    print()
    print(" OPCIÓN 1: Muestra todas las mascotas de la clínica.")
    print(" OPCIÓN 2: Muestra las mascotas y su raza por especie.")
    print(" OPCIÓN 3: Muestra el número de visitas registradas por mascota.")
    print(" OPCIÓN 4: Introduce especie y sexo. Muestra el nombre, edad y peso de las mascotas encontradas.")
    print(" OPCIÓN 5: Muestra el precio, nombre del distribuidor y teléfono de un medicamento.")
    print(" OPCIÓN 6: Introduce el numero de chip. Muestra las visitas, patología y nombre del veterinario que le atendió.")
    print(" OPCIÓN 7: Salir.")
    print()
    opcion = input("Introduce la opción deseada: ")

    if opcion == "1":

        # Listar mascotas:
        for nombre in listar_mascotas(arbol):
            print(nombre)
    
    elif opcion == "2":

        # Listar mascotas y su raza por especie:
        especie = input("Introduce la especie: ")
        for mascota in listar_mascotas_raza(arbol,especie):
            print("-Nombre: ",mascota[0], " -Raza: ",mascota[1])
    elif opcion == "3":

        # Contar visitas por mascota, mostrando nombre y especie.
        print ("MASCOTAS\tESPECIE\t\tVISITAS")
        print ("________\t________\t________")
        for m,e,v in zip (contar_visitas(arbol)[0],contar_visitas(arbol)[1],contar_visitas(arbol)[2]):
            print(m,"\t\t",e,"\t\t  ",v)
            
    
    elif opcion == "7":
        break
    else:
        print("Has introducido un valor erróneo.")
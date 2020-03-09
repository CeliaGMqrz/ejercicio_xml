# Programa principal

# Funciones
from funciones_clinicavet import *
# Definir el arbol
arbol = etree.parse('clinica_veterinaria.xml')

# Limpiar pantalla
import os 
def limpiar_continuar():
    continuar = input("...\npulsa Enter para continuar.")
        
# MENU 
while True:
    os.system('clear')
    print()
    print("___________________________CLINICAVET__________________________________")
    print()
    print(" OPCIÓN 1: Muestra todas las mascotas de la clínica.")
    print(" OPCIÓN 2: Muestra las mascotas y su raza por especie.")
    print(" OPCIÓN 3: Muestra el número de visitas registradas por mascota.")
    print(" OPCIÓN 4: Introduce especie y sexo. Muestra el nombre, edad y peso de las mascotas encontradas.")
    print(" OPCIÓN 5: Muestra el precio, nombre del distribuidor y teléfono de un medicamento.")
    print(" OPCIÓN 6: Introduce el numero de chip. Muestra las visitas, patología y nombre del veterinario que le atendió.")
    print(" SALIR: Introduce un '*'.")
    print()
    opcion = input("Introduce la opción deseada: ")

    if opcion == "1":
    # Listar mascotas:
    
        for nombre in listar_mascotas(arbol):
            print(nombre)
        limpiar_continuar()

    elif opcion == "2":
    # Listar mascotas y su raza por especie:

        especie = input("Introduce la especie: ")
        especie = especie.capitalize()

        # Validar especie
        while especie not in ("Gato","Perro"):
            print ("\nNo existe la especie indicada.")
            especie = input("Introduce la especie: ")
            especie = especie.capitalize()
        
        # Imprimir mascota y raza
        print ()
        print ("MASCOTAS      RAZA  ")
        print ("________    ________")
        for mascota in listar_mascotas_raza(arbol,especie):
            print("-",mascota[0],"     -",mascota[1])
        limpiar_continuar()


    elif opcion == "3":
    # Contar visitas por mascota, mostrando nombre y especie.
        
        print ("MASCOTAS\tESPECIE\t\tVISITAS")
        print ("________\t________\t________")
        for m,e,v in zip (contar_visitas(arbol)[0],contar_visitas(arbol)[1],contar_visitas(arbol)[2]):
            print(m,"\t\t",e,"\t\t  ",v)
        limpiar_continuar()

    elif opcion == "4":
    # Recibe por teclado la especie y el sexo, y muestra el nombre, la edad y peso de las mascotas registradas.
        
        especie = input("Introduce la especie: ")
        especie = especie.capitalize()

        # Validar especie
        while especie not in ("Gato","Perro"):
            print ("\nNo existe la especie indicada.")
            especie = input("Introduce la especie: ")
            especie = especie.capitalize()

        sexo = input("Introduce el sexo: ")
        
        # Validar sexo        
        while sexo not in ("h","m"):
            print("\nValor incorrecto. Introduce 'h' (hembra) o 'm' (macho).")
            sexo = input("Introduce el sexo:")

        # Mostrar nombre, edad y peso
        print("MASCOTA\tEDAD\tPESO")
        print("______  _____\t______")
        for nombre,edad,peso in zip (filtrar_mascotas(arbol,especie,sexo)[0],filtrar_mascotas(arbol,especie,sexo)[1],filtrar_mascotas(arbol,especie,sexo)[2]):
            print(nombre,"\t",edad,"\t",peso)
        limpiar_continuar()

    
    elif opcion == "5":
    # Recibe por teclado el nombre de un medicamento registrado, muestra el precio y el nombre y telefono de su distribuidor.

        medicamento = input("Introduce el nombre del medicamento: ")
        medicamento = medicamento.title()
        
        #validar medicamentos
        lista = info_medicamento(arbol,medicamento)[3]
        while medicamento not in lista:
            print ("\nEl medicamento indicado no existe.")
            medicamento = input("Introduce el nombre del medicamento: ")
            medicamento = medicamento.title()
        
        #mostrar precio,nombre del laboratorio y telefono
        for p,l,t in zip (info_medicamento(arbol,medicamento)[0],info_medicamento(arbol,medicamento)[1],info_medicamento(arbol,medicamento)[2]):
            
            print("\n- Precio del fármaco: ",p)
            print("- Nombre del laboratorio: ",l)
            print("- Teléfono de contacto: ",t)
        limpiar_continuar()

    elif opcion == "6":
    # Recibe el número de chip y devuelve el id de la visita y su patologia
        chip = input("\nIntroduce el numero de chip: ")
        print(mostrar_visitas_mascota(arbol,chip))
        #for visita,pat in zip (mostrar_visitas_mascota(arbol,chip)[0],mostrar_visitas_mascota(arbol,chip)[1]):
        #    print (pat)
        limpiar_continuar()
    
    
    elif opcion == "*":
        print("Programa terminado.")
        break

    else:
        print("Has introducido un valor erróneo.")
        limpiar_continuar()

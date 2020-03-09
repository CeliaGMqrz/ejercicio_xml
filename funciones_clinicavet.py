from lxml import etree

#1.Listar(basico): Esta función listará todas las mascotas de la clínica.

def listar_mascotas(arbol):
    mascotas = arbol.xpath('//mascotas/mascota/nombre/text()')
    return mascotas

#2.Listar: Lista las mascotas y su raza registradas en la clínica. La función recibe un parámetro(especie: Perro o Gato) por 
# teclado para afinar la búsqueda.

def listar_mascotas_raza(arbol,especie):
    nombres_mascota=[]
    for mascota in arbol.xpath('//mascotas/mascota[especie="%s"]'%especie):
        nombres_mascota = mascota.xpath('//mascotas/mascota[especie="%s"]/./nombre/text()'%especie)
        razas_mascota = mascota.xpath('//mascotas/mascota[especie="%s"]/./raza/text()'%especie)
        nombres_mascotas = list((nombres_mascota))
        razas_mascotas = list ((razas_mascota))
    return zip(nombres_mascotas,razas_mascotas)


#3.Contar: Lista todas las mascotas y cuenta cuantás visitas se han registrado de cada una, mostrar el nombre, la especie  
# y el número de visitas de cada una.

def contar_visitas(arbol):
    # Creamos las listas que vamos a utlizar para devolver los resultados
    lista_visitas = []
    nombres_mascota = []
    especies_mascota = []
    # Sacamos el nombre de las mascotas
    mascotas = arbol.xpath('//mascotas/mascota/nombre/text()')
    nombres_mascota = list(mascotas)
    # Sacamos la especie de las mascotas
    especies = arbol.xpath('//mascotas/mascota/especie/text()')
    especies_mascota = list(especies)
    # Contamos las visitas registradas por cada mascota
    for visita in arbol.xpath('//mascotas/mascota'):
        visitas = int(visita.xpath('count(.//visita)'))
        lista_visitas.append(visitas)
    # Añadimos a una lista las listas obtenidas
    conjunto = [nombres_mascota,especies_mascota,lista_visitas]
    return conjunto


#4.Flitrar: La función recibe dos parámetros (especie(gato,perro) y sexo(h,m)) y muestra el nombre, la edad y el peso 
# de las mascotas econtradas.

def filtrar_mascotas(arbol,especie,sexo):
    
    for mascota in arbol.xpath('//mascotas/mascota[especie="%s" and sexo="%s"]'%(especie,sexo)):
        nombres_mascota = mascota.xpath('//mascotas/mascota[especie="%s" and sexo="%s"]/./nombre/text()'%(especie,sexo))
        edad_mascota = mascota.xpath('//mascotas/mascota[especie="%s" and sexo="%s"]/./edad/text()'%(especie,sexo))
        peso_mascota = mascota.xpath('//mascotas/mascota[especie="%s" and sexo="%s"]/./peso/text()'%(especie,sexo))

    filtro = [nombres_mascota,edad_mascota,peso_mascota]
    return filtro

 
#Funciones para validar especie y sexo
def validar_especie(especie):
    while especie not in ("Gato","Perro"):
        print ("\nNo existe la especie indicada.")
        especie = input("Introduce la especie: ")
        especie = especie.capitalize()
    return especie

def validar_sexo(sexo):
    while sexo not in ("h","m"):
        print("\nValor incorrecto. Introduce 'h' (hembra) o 'm' (macho).")
        sexo = input("Introduce el sexo:")
        sexo = sexo.lower()

#5.Informacion relacionada: La función recibe por teclado el nombre de un medicamento y muestra su precio pero además 
# muestra el nombre del laboratorio que lo distribuye y el teléfono.

#6.Libre: Pide por teclado el número de chip de la mascota y muestra todas las visitas con la patología y el nombre del 
# veterinario que le atendió en cada visita.





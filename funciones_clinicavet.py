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
    lista_visitas = []
    nombres_mascota = []
    especies_mascota = []
    mascotas = arbol.xpath('//mascotas/mascota/nombre/text()')
    nombres_mascota = list(mascotas)
    especies = arbol.xpath('//mascotas/mascota/especie/text()')
    especies_mascota = list(especies)
    for visita in arbol.xpath('//mascotas/mascota'):
        visitas = int(visita.xpath('count(.//visita)'))
        lista_visitas.append(visitas)
    conjunto = [nombres_mascota,especies_mascota,lista_visitas]
    return conjunto


#4.Flitrar: La función recibe dos parámetros (especie(gato,perro) y sexo(h,m)) y muestra el nombre, la edad y el peso 
# de las mascotas econtradas.
 
#5.Informacion relacionada: La función recibe por teclado el nombre de un medicamento y muestra su precio pero además 
# muestra el nombre del laboratorio que lo distribuye y el teléfono.

#6.Libre: Pide por teclado el número de chip de la mascota y muestra todas las visitas con la patología y el nombre del 
# veterinario que le atendió en cada visita.





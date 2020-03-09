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

 
#5.Informacion relacionada: La función recibe por teclado el nombre de un medicamento y muestra su precio pero además 
# muestra el nombre del laboratorio que lo distribuye y el teléfono.

def info_medicamento(arbol,medicamento):
    
    #Usaremos los nombres de todos los medicamentos para validar la entrada de datos
    medicamentos = arbol.xpath('//medicamentos/medicamento/nombre/text()')
    
    #Extraer el precio, nombre del laboratorio y telefono segun el medicamento indicado.
    precio = arbol.xpath('//medicamentos/medicamento[nombre="%s"]/./precio/text()'%medicamento)
    laboratorio = arbol.xpath('//medicamentos/medicamento[nombre="%s"]//../../../nombre/text()'%medicamento)
    telefono = arbol.xpath('//medicamentos/medicamento[nombre="%s"]//../../../telefono/text()'%medicamento)
    
    #Filtrar la informacion
    filtro = [precio,laboratorio,telefono,medicamentos]
    return filtro

#6.Libre: Pide por teclado el número de chip de la mascota y muestra todas las visitas con la patología y el nombre del 
# veterinario que le atendió en cada visita.

def mostrar_visitas_mascota(arbol,chip):
    
    #Para validar la entrada de numero de chip
    numero_chip = arbol.xpath('//mascotas/mascota/numChip/text()')

    #Crear lista para los nombres de los veterinarios
    vetes = []
    for mascota in arbol.xpath('//mascotas/mascota[numChip="%s"]'%chip):
        visitas = mascota.xpath('//mascotas/mascota[numChip="%s"]/./visitas/visita/@id'%chip)
        patologias = mascota.xpath('//mascotas/mascota[numChip="%s"]/./visitas/visita/patologia/text()'%chip)
        fechas = mascota.xpath('//mascotas/mascota[numChip="%s"]/./visitas/visita/fecha/text()'%chip)
        ides = mascota.xpath('//mascotas/mascota[numChip="%s"]/./visitas/visita/veterinario/text()'%chip)
    #vetes = list(ides)
    #for i in vetes:

    #Recorrer en la estructura veterinario para obtener el nombre de los veterinarios
    #for vet in arbol.xpath('//veterinarios/veterinario'):
    #    nombres_vet = vet.xpath('//veterinarios/veterinario/nombre/text()//../@id[contains(text(),"%s")]'%id)
   

    #for veterinario in arbol.xpath('//veterinarios/veterinario/@id')
    
    filtro = [visitas,patologias,fechas,ides,vetes]
    return filtro




def leer_camion(nombre_archivo):  #Define la función
    with open(nombre_archivo,'rt') as contenido_camion:    
        encabezados = next(contenido_camion) #Saltea la línea de encabezados
        lista_camion = []   #Crea una lista vacía para usar después
        
        for linea in contenido_camion:  #Abre un ciclo para cada linea del archivo
            linea_list = linea.split(',') #Transforma la cadena en una lista
            linea_dic = {
                'nombre':linea_list[0],
                'cajones':linea_list[1],
                'precio':linea_list[2]
                } #Transforma la lista en diccionario
            lista_camion += [linea_dic] #Agrega la tupla como elemento de la lista
        return lista_camion # Guarda la lista de diccionarios
            
costo = leer_camion('../Data/camion.csv')

def leer_precios(nombre_archivo): #Define la función
    with open(nombre_archivo) as precios_camion: #Abre el archivo
        import csv
        lista_precios = csv.reader(precios_camion)
        encabezados = next(lista_precios) #Saltea la línea de encabezados
        precios_dic={}   #Abre una lista vacía para llenar con el for
        
        for linea in lista_precios:
            try:  # Abre un try para que evite los IndezError por casillas vacías
                fruta = linea[0]
                precio = linea[1]
                precios_dic[fruta] = precio
            except IndexError:
                pass
        return precios_list_dic # Guarda la lista de diccionarios
        
beneficio = leer_precios('../Data/precios.csv')

# Ni la menor idea como hacer el balance con los diccionarios
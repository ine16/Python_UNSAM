from pprint import pprint 
import csv

def leer_camion(nombre_archivo): # lee el archivo camion.csv y hace una lista de diccionarios
    camion_lista = []
    camion_lista2 = []
    with open(nombre_archivo,"rt",encoding=("UTF8")) as datos: 
        next(datos)
        for line in datos:
            linea = line.split(",")
            try:
                camion_lista = [("nombre",linea[0]),("cajones",int(linea[1])),("precios",float(linea[2]))]
                camion_lista2.append(dict(camion_lista))
            except IndexError:
                print("Fuera de rango")
    return camion_lista2

def leer_precios(nombre_archivo2): ## lee el archivo precios y devuelve un diccionario
   precios = {}
   f = open(nombre_archivo2,"rt",encoding=("UTF8"))
   rows = csv.reader(f)
   for row in rows:
       try:
           precios[row[0]] = row[1]
       except IndexError:
           print("\nFuera de rango\n")
   f.close()
   return precios

nombre_archivo = "..\Data\camion.csv" ## se establece la ruta
nombre_archivo2 = "..\Data\precios.csv" ## se establece la ruta

camion = leer_camion(nombre_archivo) # se llama a la funcion y se guarda el valor en la variable
pprint(camion) # se imprime la lista

total = 0.0
for dato in camion:
    total += dato["cajones"]*dato["precios"]
print("\nEl costo total es: $",total,"\n")

precios = leer_precios(nombre_archivo2) # se llama a la funcion y se guarda en la variable
pprint(precios) # se imprime el diccionario

costo = 0
venta = 0
ganancia = 0
for frutas in precios: # se realiza una busqueda
    for clave in camion:
        if clave["nombre"] == frutas:
           costo += clave["cajones"]*clave["precios"]
        if clave["nombre"] == frutas:
           venta += float(precios[frutas]) * clave["cajones"]

ganancia = (venta - costo) ## Se calcula la ganancia si es negativo es que hay perdida

if(ganancia > 0):
    print(f"\nHubo una ganancia de: ${round(ganancia,2)}\n")
else:
    print(f"\nHubo una perdida de: ${round(ganancia,2)*-1}\n")
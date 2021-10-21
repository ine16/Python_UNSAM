# Ejercicio 2.7: Buscar precios

def buscar_precio(fruta):
	F = fruta[0].upper()
	ruta = fruta[1:].lower()
	string_Fruta = F + ruta
	f = open('C:/Users/Ine/Desktop/Doctorado/ejercicios_python/Data/precios.csv', 'rt', encoding='utf8')
	precio=0
	for line in f:
	    row = line.split(',')
	    if row[0] == string_Fruta:
	    	precio = float(row[1])
	    	print(f'El precio de un cajón de {string_Fruta} es: {precio}')
	    	break
	f.close()
	if precio == 0:
		print(f'{string_Fruta} no figura en el listado de precios.')
	return

## SALIDAS AL CORRER LA FUNCION DE FORMA INTERACTIVA
# >>> buscar_precio('frambuesa')
# El precio de un cajón de Frambuesa es: 34.35
# >>> buscar_precio('kale')
# Kale no figura en el listado de precios.
# >>> buscar_precio('kiwi')
# Kiwi no figura en el listado de precios.
# >>> buscar_precio('rúcula')
# El precio de un cajón de Rúcula es: 36.9
f = open('C:/Users/Ine/Desktop/Doctorado/ejercicios_python/Data/precios.csv', 'rt')
for line in f:
    row = line.split(',')
    if row[0] == 'Naranja':
    	precio = float(row[1])
    	break
f.close()
print("El precio de la naranja es", precio)
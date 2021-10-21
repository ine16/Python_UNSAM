# Meto los 2 ejemplos de "Atrapar y administrar excepciones" en el mismo archivo
ejemplo=1 #0 corresponde al primer ejemplo, 1 al otro

if ejemplo==0:
	numero_valido=False
	while not numero_valido:
	    try:
	        a = input('Ingresá un número entero: ')
	        n = int(a)
	        numero_valido = True
	    except ValueError:
	        print('No es válido. Intentá de nuevo.')
	print(f'Ingresaste {n}.')
else:
	numero_valido=False
	while not numero_valido:
	    try:
	        a = input('Ingresá un número entero: ')
	        n = int(a)
	        numero_valido = True
	    except:
	        print('No es válido. Intentá de nuevo.')
	print(f'Ingresaste {n}.')
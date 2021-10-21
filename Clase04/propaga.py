def se_propaga(lista, pos_uno):
	'''
	Propaga a izquierda y derecha de la posición donde hay un 1 (pos_uno) hasta toparse con un -1 o hallarse en la
	posición inicial o final de la lista. Devuelve la posición más a la derecha que contiene un -1 si lo hay,
	caso contrario devuelve la última posición de la lista
	'''	

	# 3 casos posibles: el 1 está en el extremo izquierdo de la lista, en el derecho o está en algún lugar en el medio
	# Según cuál sea entrará a uno de los while o a ambos
	
	# Empiezo a evaluar en la posición anterior a donde tenía el 1
	pos_anterior = pos_uno - 1
	
	while pos_anterior >= 0 and lista[pos_anterior] != -1:
		# Modifico el valor directamente para no añadir un if de más, ya que si valía 0 pasa a valer 1 y si valía 1 queda en 1
		lista[pos_anterior] = 1
		pos_anterior -= 1


	# Empiezo a evaluar en la posición siguiente a donde tenía el 1
	pos_siguiente = pos_uno + 1
	pos_final = len(lista) - 1 # indice del último elemento de la lista ingresada
	
	while pos_siguiente <= pos_final and lista[pos_siguiente] != -1:
		lista[pos_siguiente] = 1
		pos_siguiente += 1
	
	return pos_siguiente



def propagar(L):
	'''
	Recibe una lista L con 0's, 1's y -1's y devuelve una lista en la que los 1's se propagaron a sus vecinos con 0.
	'''

	# Inicio la búsqueda de 1's en el primer elemento (lo llamo "fósforo actual")
	fosforo_actual = 0

	# Ahora empieza a buscar 1's en la lista hasta terminarla
	fosforo_final = len(L) - 1
	while fosforo_actual <= fosforo_final:
		
		# Cuando encuentra un 1 (fósforo encendido) se propaga a ambos lados hasta encontrar un -1 (fósforo apagado)
		if L[fosforo_actual] == 1:
			
			# Luego de entrar en "se propaga", el fósforo actual pasa a ser el último índice donde hay un -1.
			# Si no encuentra un -1 es el último índice de la lista
			fosforo_actual = se_propaga(L, fosforo_actual)
		
		fosforo_actual += 1	
	
	return L
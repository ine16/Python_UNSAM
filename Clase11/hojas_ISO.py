# hojas_ISO.py

def medidas_hoja_A(N):
	'''
	Para una entrada N>0, devuelve el ancho y el largo de la hoja tamaño A(N) 
	calculada recursivamente a partir de las medidas de la hoja A(N−1) en mm, 
	usando la hoja A0 como caso base. Devuelve tupla (ancho, largo)
	'''
    if N==0:
        ancho = 841
        largo = 1189
    
    else:
    	ancho_anterior, largo_anterior = medidas_hoja_A(N-1)
    	ancho = largo_anterior//2
    	largo = ancho_anterior
    
    return (ancho, largo)

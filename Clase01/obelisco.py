# obelisco.py - ejercicio 1.4

# *CODIGO ORIGINAL*
# grosor_billete = 0.11 * 0.001 # 0.11 mm en metros
# altura_obelisco = 67.5         # altura en metros
# num_billetes = 1
# dia = 1

# while num_billetes * grosor_billete <= altura_obelisco:
#     print(dia, num_billetes, num_billetes * grosor_billete)
#     dia = dias + 1
#     num_billetes = num_billetes * 2

# print('Cantidad de días', dia)
# print('Cantidad de billetes', num_billetes)
# print('Altura final', num_billetes * grosor_billete)

# *AL CORRERLO IMPRIME:*
#Traceback (most recent call last):
#  File "C:\Users\Ine\Desktop\Doctorado\ejercicios_python\Clase01\obelisco.py", line 10, in <module>
#    dia = dias + 1
#NameError: name 'dias' is not defined

#El error está en la línea 10 y es que en vez de "dia" (variable definida antes) dice "dias" (variable no definida) 


# *CODIGO ARREGLADO*
grosor_billete = 0.11 * 0.001 # 0.11 mm en metros
altura_obelisco = 67.5         # altura en metros
num_billetes = 1
dia = 1

while num_billetes * grosor_billete <= altura_obelisco:
    print(dia, num_billetes, num_billetes * grosor_billete)
    dia = dia + 1 #cambié "dias" por "dia" para que haga lo que queremos: aumentar en 1 la variable "dia" en cada loop
    num_billetes = num_billetes * 2

print('Cantidad de días', dia)
print('Cantidad de billetes', num_billetes)
print('Altura final', num_billetes * grosor_billete)
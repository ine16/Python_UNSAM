capadepenapa = ''

cadena = input("Inserte palabra para convertir a geringoso: ")
for c in cadena:
    capadepenapa = capadepenapa + c
    if c in ['a','e','i','o','u']:
        vocal = c
        capadepenapa = capadepenapa + 'p' + vocal
print("En geringoso:",capadepenapa)

# ALGUNAS CORRIDAS
# PS C:\Users\Ine\Desktop\Doctorado\ejercicios_python\Clase01> python geringoso.py
# Inserte palabra para convertir a geringoso: geringoso
# En geringoso: geperipingoposopo
# PS C:\Users\Ine\Desktop\Doctorado\ejercicios_python\Clase01> python geringoso.py
# Inserte palabra para convertir a geringoso: batata
# En geringoso: bapatapatapa
# PS C:\Users\Ine\Desktop\Doctorado\ejercicios_python\Clase01> python geringoso.py
# Inserte palabra para convertir a geringoso: apa
# En geringoso: apapapa
# PS C:\Users\Ine\Desktop\Doctorado\ejercicios_python\Clase01> python geringoso.py
# Inserte palabra para convertir a geringoso: boligoma
# En geringoso: bopolipigopomapa
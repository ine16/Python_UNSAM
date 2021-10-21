# rebotes.py

# =====
# ENUNCIADO:
# Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 
# de la altura desde la que cayó. Escribí un programa rebotes.py que imprima una tabla mostrando las alturas 
# que alcanza en cada uno de sus primeros diez rebotes.
# =====

altura = 100 # altura inicial de la pelota medida en metros
num_rebotes = 10 # el número de rebotes para los que nos interesa saber la altura que alcanza la pelota

for rebote in range(num_rebotes):
    altura = altura*3/5
    #print((rebote+1), altura) # línea original
    print((rebote+1), round(altura,4)) # línea modificada para que imprima el número redondeado a 4 dígitos

# SALIDAS USANDO LA LÍNEA ORIGINAL
# 
# 1 60.0
# 2 36.0
# 3 21.6
# 4 12.960000000000003
# 5 7.776000000000002
# 6 4.6656
# 7 2.79936
# 8 1.679616
# 9 1.0077696
# 10 0.60466176

#SALIDA USANDO LA LÍNEA CON round()
# 
# 1 60.0
# 2 36.0
# 3 21.6
# 4 12.96
# 5 7.776
# 6 4.6656
# 7 2.7994
# 8 1.6796
# 9 1.0078
# 10 0.6047
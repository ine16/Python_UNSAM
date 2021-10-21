# Tabla de multiplicar del 1 al (N-1)
N=10

header = '     ' #le agrego este espacio a la fuerza, corresponde a los primeros 5 caracteres en linea_tabla (línea 19)

numeros = []
for i in range(1, N):
    numeros.append(i)
    header += f'{i:>3d} '


print(header)
separador = '-' * len(header)
print(separador)


for i in numeros:
    elemento = i
    linea_tabla = f'{i:>3d}: {i:>3d} ' #5 caracteres (columna fuera de la tabla) + 3 caracteres para i*1
    
    for j in range(2, N):
        elemento += i
        linea_tabla += f'{elemento:>3d} '
    
    print(linea_tabla)
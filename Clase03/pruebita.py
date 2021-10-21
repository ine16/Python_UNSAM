def tiene_uno(expresion):
    tiene = False
    try:
        n = len(expresion)
        i = 0
        while (i<n) and not tiene:
            if expresion[i] == '1':
                tiene = True
            i += 1
        return tiene
    except TypeError:
        print(f'Error al ingresar {expresion}. Por favor ingresá una cadena de caracteres: ')
        entrada_usuarie = input()
        reintento = tiene_uno(entrada_usuarie)
        return reintento

print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))
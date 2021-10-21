frase = 'todos somos programadores'
lista_frase_inclusiva=[]
palabras = frase.split()
for palabra in palabras:
    if palabra[-1]=='o' or palabra[-1]=='a':
    	palabra_modif=palabra[:-1]+'e'
    	lista_frase_inclusiva.append(palabra_modif)
    elif palabra[-1]=='s':
    	if palabra[-2]=='o' or palabra[-2]=='a':
    		palabra_modif=palabra[:-2]+'es'
    		lista_frase_inclusiva.append(palabra_modif)
    	else:
    		lista_frase_inclusiva.append(palabra)
    else:
    	lista_frase_inclusiva.append(palabra)
frase_inclusiva = ' '.join(lista_frase_inclusiva)
print(frase_inclusiva)
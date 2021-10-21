import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]



def envido_31_o_mas(tantos, mano):
	suma_cartas = tantos - 20
	envido = False
	valor,palo = mano[0]
	i=1
	if valor in valores[:7]:
		while i<=2:
			valor_2,palo_2 = mano[i]
			if palo_2 == palo and valor_2 in valores[:7] and valor+valor_2==suma_cartas:
				envido = True
				break
			i += 1
	else:
		valor_2,palo_2 = mano[1]
		valor_3,palo_3 = mano[2]
		if palo_2 == palo_3 and valor_2 in valores[:7] and valor_3 in valores[:7] and valor_3+valor_2==suma_cartas:
				envido = True
	return envido


# Simulo una partida entre 2 personas
for i in range(15):
	random.shuffle(naipes)
	cartas_repartidas = random.sample(naipes,k=6)
	mano_1 = cartas_repartidas[:3]
	print(mano_1)
	print(es_envido(31, mano_1))
	mano_2 = cartas_repartidas[3:]
	print(mano_2)
	print(es_envido(31, mano_2))
	print('\n')
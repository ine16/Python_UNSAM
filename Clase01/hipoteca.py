# hipoteca.py

## EJERCICIO 1.11: BONUS (que incluye los agregados del 1.9, 1.10 y 1.20)

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0 # va a contar los meses requeridos para pagar el monto total, inicializo el mes en 0

## variables que definen el monto extra a pagar y el mes en que inicia y termina el pago extra
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000


#titulo_tabla='Mes Total pagado  Saldo' # linea comentada para el ej 1.11, descomentar para el 1.20
#print(titulo_tabla) # linea comentada para el ej 1.11, descomentar para el 1.20
while saldo > 0:
    if saldo * (1+tasa/12) < pago_mensual:
    	pago_mensual = saldo * (1+tasa/12)
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

    if pago_extra_mes_comienzo - 1 <= mes and mes < pago_extra_mes_fin:
        saldo = saldo - pago_extra
        total_pagado = total_pagado + pago_extra

    mes = mes + 1
    print(mes, round(total_pagado, 2), round(saldo, 2)) # comentar esta linea para el ej 1.20
    #tabla=f'{mes:3d} {round(total_pagado, 2):9.2f} {round(total_pagado, 2):10.2f}' # linea comentada para el ej 1.11, descomentar para el 1.20
    #print(tabla) # linea comentada para el ej 1.11, descomentar para el 1.20

print('\nTotal pagado:', round(total_pagado, 2))
print('Meses:', mes)



## EJERCICIO 1.8
# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# mes = 0 # va a contar los meses requeridos para pagar el monto total, inicializo el mes en 0

# while saldo > 0:
#     saldo = saldo * (1+tasa/12) - pago_mensual
#     total_pagado = total_pagado + pago_mensual
#     if mes < 12:
#         saldo = saldo - 1000 # paga $1000 extra por mes desde el mes 0 hasta el 11 (es decir, los primeros 12 meses)
#         total_pagado = total_pagado + 1000
#     mes = mes + 1

# print('Total pagado', round(total_pagado, 2))
# print('Meses requeridos', mes)

# SALIDA DEL PROGRAMA PARA EL EJERCICIO 1.8
# Total pagado 929965.62
# Meses requeridos 342
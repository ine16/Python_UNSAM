f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))

####
# ¿Cómo modificarías este ejemplo para transformar la fecha (date) en una tupla como (6, 11, 2007)?
####

fecha = record['date'].split('/')
fecha_tupla = tuple(int(numero) for numero in fecha)
record['date'] = fecha_tupla
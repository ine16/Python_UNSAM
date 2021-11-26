import numpy as np
import matplotlib.pyplot as plt

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

a, b = ajuste_lineal_simple(superficie, alquiler)

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())


grilla_x = np.linspace(start = min(superficie), stop = max(superficie), num = 1000)
grilla_y = grilla_x*a + b

g = plt.scatter(x = superficie, y = alquiler)
plt.title('Gráfico de los datos y ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.xlabel('superficie')
plt.ylabel('alquiler')
plt.show()

# Corriendo en cmd:
# [ 0.55434783  0.69782609 -0.74130435 -0.51086957]
# ECM: 0.4011956521739133
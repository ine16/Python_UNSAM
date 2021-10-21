import matplotlib.pyplot as plt
import numpy as np


def plotear_temperaturas():
	temperaturas = np.load('../Data/vector_temps.npy')
	plt.hist(temperaturas,bins=20)
	plt.show()

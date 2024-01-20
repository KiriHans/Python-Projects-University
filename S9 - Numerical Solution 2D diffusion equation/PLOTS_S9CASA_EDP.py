import numpy as np
import matplotlib.pylab as plt

L = 1
M = 100
dx = L / M

# Graficar mapa de calor en t = 0, 100, 1000, 2500

dataHeat = np.genfromtxt("difusion.txt")

intervalx = np.arange(0, 1 + dx/2, dx)
intervaly = np.arange(0, 1 + dx/2, dx)

intervaly, intervalx = np.meshgrid(intervalx, intervaly)

array = dataHeat[:, 1:]

for i in range(4):
    array2 = dataHeat[i:i+1, 1:].reshape(100, 100)
    plt.figure()
    plt.pcolormesh(intervalx, intervaly, array2)
    plt.colorbar()
    plt.savefig(f"ecuacion_de_calor_{i}.png")
    plt.close()

import numpy as np
import matplotlib.pylab as plt


array = np.genfromtxt("datos1.txt")
size_array = array.size
axis_x = np.arange(size_array)


plt.scatter(axis_x, array)
plt.savefig("aleatorios.png")
plt.close()

# --------------------------------------------

array = np.genfromtxt("datos2.txt")
size_array = array.size
axis_x = np.arange(size_array)

plt.scatter(axis_x, array)
plt.savefig("aleatorios_con_impares.png")
plt.close()

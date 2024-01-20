import math
import numpy as np
import matplotlib.pylab as plt


# Graficando usando los puntos calculados del método de Euler

dataEuler = np.genfromtxt("euler_array.txt")
interval = dataEuler[:, :1]
eulerArray = dataEuler[:, 1:]

plt.figure
plt.plot(interval, eulerArray)
plt.savefig("euler_method.png")
plt.close()

# # --------------------------------------------

# Graficando usando los puntos calculados del método de Runge-Kutta

dataRunge = np.genfromtxt("runge_array.txt")
interval = dataRunge[:, :1]
intervalSize = interval.size
rungeKuttaArray = dataRunge[:, 1:]

plt.figure
plt.plot(interval, rungeKuttaArray)
plt.savefig("runge-Kutta_method.png")
plt.close()

# # --------------------------------------------

# Graficando usando los puntos calculados de la solución analítica


def analiticFunction(t):
    return np.exp(-t)


analiticalArray = analiticFunction(interval)

plt.figure
plt.plot(interval, analiticalArray)
plt.savefig("analitical_graph.png")
plt.close()


# # --------------------------------------------

# Comparando la solución analítica con el método de Euler

plt.figure()
f, ax = plt.subplots()
ax.plot(interval, analiticalArray, "g", label="Analitical method")
ax.plot(interval, eulerArray, "r--",  label="Euler method")
plt.legend()
plt.savefig("comparacion_euler_analitica.png")
plt.close()

# # --------------------------------------------

# Comparando la solución analítica con el método de Runge-Kutta

plt.figure()
f, ax = plt.subplots()
ax.plot(interval, analiticalArray, "g", label="Analitical method")
ax.plot(interval, rungeKuttaArray, "b--",  label="Runge-Kutta method")
plt.legend()
plt.savefig("comparacion_Runge-Kutta_analitica.png")
plt.close()

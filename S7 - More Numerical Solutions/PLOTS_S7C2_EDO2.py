import math
import numpy as np
import matplotlib.pylab as plt


# Graficando usando los puntos calculados del método de Euler

dataEuler = np.genfromtxt("euler_array.txt")
interval = dataEuler[:, :1]
positionArray = dataEuler[:, 1:2]
velocityArray = dataEuler[:, 2:]

plt.figure()
f, ax = plt.subplots()
ax.plot(interval, positionArray, "g", label="position")
ax.plot(interval, velocityArray, "r--",  label="velocity")
plt.legend()
plt.savefig("euler_method.png")
plt.close()

# # --------------------------------------------

# Graficando usando los puntos calculados del método de Runge-Kutta

dataRunge = np.genfromtxt("runge_array.txt")
interval = dataRunge[:, :1]
positionArray = dataRunge[:, 1:2]
velocityArray = dataRunge[:, 2:]

plt.figure()
f, ax = plt.subplots()
ax.plot(interval, positionArray, "g", label="position")
ax.plot(interval, velocityArray, "r--",  label="velocity")
plt.legend()
plt.savefig("runge-Kutta_method.png")
plt.close()



# # --------------------------------------------

# Graficando usando leapFrog array

dataLeap = np.genfromtxt("leapFrog_array.txt")
interval = dataLeap[:, :1]
positionArray = dataLeap[:, 1:2]
velocityArray = dataLeap[:, 2:]

plt.figure()
f, ax = plt.subplots()
ax.plot(interval, positionArray, "g", label="position")
ax.plot(interval, velocityArray, "r--",  label="velocity")
plt.legend()
plt.savefig("leap-Frog_method.png")
plt.close()

# # --------------------------------------------

# Graficando usando los puntos calculados de la solución analítica


def analiticFunction(t, k, m):
    return (0.1)*np.cos(np.sqrt(k/m)*t)

def difAnaliticFunction(t, k, m):
    return -(np.sqrt(k/m))*(0.1)*np.sin(np.sqrt(k/m)*t)


analiticalPosition = analiticFunction(interval, 50, 0.2)
analiticalVelocity = difAnaliticFunction(interval, 50, 0.2)


f, ax = plt.subplots()
ax.plot(interval, analiticalPosition, "g", label="position")
ax.plot(interval, analiticalVelocity, "r--",  label="velocity")
plt.legend()
plt.savefig("analitical_graph.png")
plt.close()


# # --------------------------------------------

# Graficando un oscilador amortiguado usando Euler

dataEuler = np.genfromtxt("euler_amortiguado_array.txt")
interval = dataEuler[:, :1]
positionArray = dataEuler[:, 1:2]
velocityArray = dataEuler[:, 2:]

plt.figure()
f, ax = plt.subplots()
ax.plot(interval, positionArray, "g", label="position")
ax.plot(interval, velocityArray, "r--",  label="velocity")
plt.legend()
plt.savefig("euler_method_amortiguado.png")
plt.close()





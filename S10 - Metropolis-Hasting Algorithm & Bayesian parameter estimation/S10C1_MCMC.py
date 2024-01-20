# Ejercicio 1

import numpy as np
import matplotlib.pylab as plt


# Use esta funcion que recibe un valor x y retorna un valor f(x) donde f es la forma funcional que debe seguir su distribucion. 
def mifun(x):
  x_0 = 3.0
  a = 0.01
  return np.exp(-(x**2))/((x-x_0)**2 + a**2)

# Dentro de una funcion que reciba como parametros el numero de pasos y el 
# sigma de la distribucion gausiana que va a usar para calcular el paso de su 
# caminata, implemente el algortimo de Metropolis-Hastings. Finalmente, 
# haga un histograma de los datos obtenidos y grafique en la misma grafica, 
# la funcion de distribucion de probabilidad fx

# Cuando haya verificado que su codigo funciona, use los siguientes parametros:
# sigma = 5, pasos =100000 
# sigma = 0.2, pasos =100000 
# sigma = 0.01, pasos =100000 
# sigma = 0.1, pasos =1000 
# sigma = 0.1, pasos =100000 
# este puede ser muy demorado dependiendo del computador: sigma = 0.1, pasos =500000 

# Al ejecutar el codigo, este debe generar 6 (o 5) graficas .pdf una para cada vez que se llama a la funcion.
  

def calcDist(pasos, sigma):
  arr = np.zeros(pasos)
  x_init = 8*np.random.rand(1)-4
  arr[0] = x_init
  for i in range(1, pasos):
     x_new = np.random.normal(x_init, sigma)
     alpha = mifun(x_new)/mifun(x_init)
     if(alpha > 1):
       arr[i] = x_new
       x_init = x_new
     else:
       b = np.random.uniform(0,1)
       if b < alpha:
         arr[i] = x_new
         x_init = x_new
       else: 
         arr[i] = x_init
  return arr
       
# sigma = 5, pasos =100000 
sigma, pasos = 5, 100000 
interval = np.arange(-4,4, 0.01)
plt.figure()

plt.plot(interval, mifun(interval), '--r')
plt.hist(calcDist(pasos, sigma), density=True)
plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf")
plt.close()

# sigma = 0.2, pasos =100000 
sigma, pasos = 0.2, 100000 
interval = np.arange(-4,4, 0.01)
plt.figure()

plt.plot(interval, mifun(interval), '--r')
plt.hist(calcDist(pasos, sigma), density=True)
plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf")
plt.close()

# sigma = 0.01, pasos =100000 
sigma, pasos = 0.01,100000 
interval = np.arange(-4,4, 0.01)
plt.figure()

plt.plot(interval, mifun(interval), '--r')
plt.hist(calcDist(pasos, sigma), density=True)
plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf")
plt.close()

# sigma = 0.1, pasos =1000
sigma, pasos = 0.1, 1000
interval = np.arange(-4,4, 0.01)
plt.figure()

plt.plot(interval, mifun(interval), '--r')
plt.hist(calcDist(pasos, sigma), density=True)
plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf")
plt.close()

# sigma = 0.1, pasos =100000
sigma, pasos = 0.1, 100000
interval = np.arange(-4,4, 0.01)
plt.figure()

plt.plot(interval, mifun(interval), '--r')
plt.hist(calcDist( pasos, sigma), density=True)
plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf")
plt.close()

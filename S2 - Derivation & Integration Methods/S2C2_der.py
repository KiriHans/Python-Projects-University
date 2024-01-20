# Derivación: Ejercicios 
# Ejercicio 1

import numpy as np
import matplotlib.pylab as plt

def funcion(x):
    return np.cos(x)

M = 99999
a = 0
b = np.pi*2
x_0 = np.linspace(a, b, M)
yx_0 = funcion(x_0)
print("yx:", yx_0)

# 1a.) Implemente el algoritmo que le permita calcular la derivada de la 
# función para los puntos en el intervalo 0 a 2pi usando forward difference
    

def forwardDifference(x, yx):
  return (yx[1:] - yx[:-1]) / (x[1] - x[0])

resultado_forwardDifference = forwardDifference(x_0,yx_0)
print(f"El resultado usando forward difference es: {resultado_forwardDifference}")

# 1b.) Implemente el algoritmo que le permita calcular la derivada de la 
# función para los puntos en el intervalo 0 a 2pi usando diferencia central.

def centralDifference(x, yx):
  return (yx[2:] - yx[:-2]) / (x[2] - x[0])

resultado_centralDifference = centralDifference(x_0,yx_0)
print(f"El resultado usando central difference es: {resultado_centralDifference}")

# 1c.) Haga una gráfica de la función y sus derivadas obtenidas usando los dos 
# métodos antes mencionado. Guarde dicha gráfica sin mostrarla en DerivadaFun.pdf

plt.plot(x_0, funcion(x_0), 'r--')


plt.plot(x_0[:-1], forwardDifference(x_0,yx_0), 'bs')


plt.plot(x_0[:-2], centralDifference(x_0,yx_0), 'g^')


plt.savefig('DerivadaFun.png')
plt.close()


# 1d). Haga una grafica con dos subplots (uno por cada metodo) del error 
# |(valor numérico - valor analitico)/valor analitico| en el intervalo. Guarde dicha gráfica sin mostrarla en ErrorDerivada.pdf

valor_analitico = - np.sin(x_0)


errorForward = np.abs((valor_analitico[1:-1] - resultado_forwardDifference[1:])/(valor_analitico[1:-1]))
errorCentral = np.abs((valor_analitico[1:-2] - resultado_centralDifference[1:])/(valor_analitico[1:-2]))

plt.figure(1)

plt.subplot(211)
plt.plot(x_0[1:-1], errorForward, 'r--')
plt.subplot(212)
plt.plot(x_0[1:-2], errorCentral, 'g--')

plt.savefig('ErrorDerivada.png')
plt.close()

# 1e). Implemente el algoritmo que le permita calcular la segunda derivada de la 
# función en el intervalo 0 a 2pi. Haga una gráfica de la función
# y su segunda derivada. Guarde dicha gráfica sin mostrarla en 2DerivadaFun.pdf.

def segundaDerivada(x, yx):
  h2 = np.square(x[1] - x[0])
  return ((yx[2:] + yx[:-2]) - 2*yx[1:-1]) / h2

plt.figure(2)

plt.subplot(211)
plt.plot(x_0, yx_0, "r--")
plt.ylabel("Función original cos(x)")

plt.subplot(212)
plt.plot(x_0[1:-1], segundaDerivada(x_0,yx_0), "g--")
plt.ylabel("Segunda derivada -cos(x)")

plt.savefig("2DerivadaFun.pdf")
plt.close()

# ----------------------------------------------------------------------


# Ejercicio 2:
# La idea de este ejercicio es que exploren la convergencia del método de 
# Newton-Raphson para encontrar los ceros del siguiente polinomio:

def poli(x):
  return (x**5)-(2.0*x**4)-(10.0*x**3)+(20.0*x*x)+ (9.0*x)-18.0

# Para esto:
# 1a.) Haga una grafica del polinomio en el intervalo [-4:4].Guarde dicha 
# gráfica sin mostrarla.

c = -4
d = 4
W = 0.1
t = np.arange(c, d, W)
plt.figure(3)

plt.subplot(211)
plt.plot(t, poli(t), "r--", t, np.zeros(t.shape), "b")
plt.savefig("NRpoli.pdf")
plt.close("all")

# 1b.) Usando su implementación de Newton-Raphson, imprima el valor de una 
# raíz x0_r del polinomio encontrada si usa como x_guess inicial
# el valor -3. Imprima el valor de x0_r encontrado y de f(x0_r)

def funcion(xx):
  return np.cos(xx)

x_guess = -3
error = 10**(-5)

def derivadaFuncion(xx):
  return -np.sin(xx)

def newtonRaphson(guess, e, repetitions = 100000):
  for _ in range(repetitions):
    fguess = funcion(guess)
    dguess = derivadaFuncion(guess)
    
    if np.abs(fguess) < e:
      return guess

    deltaX = -fguess/dguess
    guess = guess + deltaX
  print("No se encontró una raíz")


x0_r = newtonRaphson(x_guess, error)
print(f"El valor de x0_r es {x0_r}, y su imagen f(x0_r) es {funcion(x0_r)}")
 


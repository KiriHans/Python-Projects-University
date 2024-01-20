## Integración: Ejercicios
# Ejercicio 1

# Este ejercicio preparatorio busca que usted implemente correctamente tres métodos de integración numérica. Haga este
#ejercicio después de haber leído y entendido los algoritmos correspondientes a los distintos métodos. Si termina el ejercicio 2
#antes de que acabe la clase, repita el proceso para el método de Monte Carlo y el método del valor medio.

import numpy as np
import matplotlib.pylab as plt
# Función a integrar

def funcion(x1):
    return np.cos(x1)


#El intervalo de integración es de 0 a 3pi/2. Divida el intervalo de integración en M secciones para calcular sus integrales.

M = 9999
a = 0
b = 1.5*np.pi
intervalo = np.linspace(a, b, M)
valores = funcion(intervalo)

# 1a). Usando el método de suma de rectángulos, calcule la integral de la función. Compare su valor obtenido numéricamente
# con el valor analitico e imprima ambos valores.


h = intervalo[1] - intervalo[0]
integral1 = h*np.sum(valores)

valor_analitico = np.sin((3*np.pi)/2) - np.sin(0)
print(f"el valor analitico es {valor_analitico}")
print(f"el valor de la integral con el primer método es {integral1}\n")

print("----------------------------------------")
# 1b). Usando el método de trapezoide, calcule la integral de la función. Compare su valor obtenido numéricamente con el valor
# analitico e imprima ambos valores.


h = intervalo[1] - intervalo[0]
integral2 = h*((valores[0] + valores[-1])/2 + np.sum(valores[1:-1])) 
print(f"el valor analitico es {valor_analitico}")
print(f"el valor de la integral con el segundo método es {integral2}")


print("----------------------------------------")
# 1c). Usando el método de Simpson, calcule la integral de la función. Compare su valor obtenido numéricamente con el valor
# analitico e imprima ambos valores.


h = intervalo[1] - intervalo[0]

integral3 = h*((valores[0] + valores[-1]) + 4*np.sum(valores[1::2]) + 2*np.sum(valores[2::2]))/3 

print(f"el valor analitico es {valor_analitico}")
print(f"el valor de la integral con el tercer método es {integral3}")

#--------------------------------------------------------------------------------------------------
# Usando montecarlos
from numpy.random import default_rng


area_montecarlo = np.array([])
for _ in range(50):
  rng = default_rng()
  muestraX = b*rng.random((M,),)
  muestraY = 4*rng.random((M,)) - 2
  img_muestra = funcion(muestraX) 

  yp = muestraY[img_muestra > 0]
  yn = muestraY[img_muestra < 0]

  positive_area_pondering = np.count_nonzero(yp[yp >= 0] < img_muestra[img_muestra > 0][yp >= 0])
  negative_area_pondering = np.count_nonzero(yn[yn <= 0] > img_muestra[img_muestra < 0][yn <= 0])
  

  area_montecarlo = np.append(area_montecarlo, ((positive_area_pondering - negative_area_pondering)/(M))*4*(b-a))

mean_area_montecarlo = np.mean(area_montecarlo)
print(f"El valor de la integral usando el método de montecarlo es {mean_area_montecarlo}")


# /////////////////////////////////////////////////////////////

# Método del valor medio

valor_medio = (b - a)*np.sum(valores)/M
print(f"El valor de la integral usando el método del valor medio es {valor_medio}")




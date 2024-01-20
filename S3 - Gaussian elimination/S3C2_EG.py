#Ejercicio
#Escriba un código de eliminación Gaussiana para resolver el sistema Ax=B.
# Importanto los paquetes requeridos
import numpy as np

#Definiendo las constantes
N=6

#Creando las matrices y el vector de forma aleatoria
Arreglo=(np.random.random((N,N))*10.0)-5.0
B=(np.random.random((N,1))*10.0)-5.0

#Copias de la matriz y vector original
ArregloCopy = np.copy(Arreglo)
BCopy = np.copy(B)
#Calculo usando eliminación gaussiana
for i in range(Arreglo.shape[0]):
    B[i] = B[i]/Arreglo[i,i]
    Arreglo[i,:] = Arreglo[i,:]/Arreglo[i,i]
    for j in range(i+1, Arreglo.shape[1]):
        B[j] = B[j] - B[i] * Arreglo[j,i]
        Arreglo[j,:] = Arreglo[j,:] - Arreglo[i,:] * Arreglo[j,i]
        
print(Arreglo)
print("=")
print(B)
print("_----")

for i in range(Arreglo.shape[0] - 1):
    B[-2-i] = 2*B[-2-i] - np.dot(Arreglo[-2-i, :], B[:,0])
        
print("Usando eliminación Gaussiana para resolver el sistema de ecuaciones lineales:")
print(B)

#Calculo usando los paquetes de numpy
x = np.linalg.solve(ArregloCopy, BCopy)  
print("\nUsando el paquete de numpy:")
print(x)

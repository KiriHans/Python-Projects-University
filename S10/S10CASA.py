# Ejercicio 1 Terminar lo que hizo en clase + dos preguntas adicionales (en mayusculas en el texto)

import numpy as np
import matplotlib.pylab as plt
import math


# 1) lea los datos de resorte.dat y almacenelos.
#

data = np.genfromtxt("resorte.dat")

t_data = data[:, :1]
value_data = data[:, 1:]
a = np.array([1, 2])
size_value_data = value_data.size
value_data_test = np.copy(value_data)
t_data_test = np.copy(t_data)
value_data_test.shape = 200
t_data_test.shape = 200

# Los datos corresponden a las posiciones en x de un oscilador (masa resorte)
# en funcion del tiempo. La ecuacion de movimiento esta dada por
# xt=a*np.exp(-gamma*t)*np.cos(omega*t)
# Donde a, gamma, y omega son parametros que se busca determinar.

# 2) Implemente un algoritmo que le permita, por medio de estimacion bayesiana
# de parametros, encontrar los parametros correspondientes a los datos d. Para esto debe:

# 2a.) definir una funcion que reciba los parametros que se busca estimar y
# los datos de tiempo y retorne los datos modelados


def model(t, a, gamma, omega):
    return a*np.exp(-gamma*t)*np.cos(omega*t)

# 2b.) Definir una funcion que retorne la funcion de verosimilitud


def chi(x_obs, x_model):
    return np.sum(np.square(x_obs - x_model))


def verosimilitud(x_obs, x_model):
    return np.exp(-0.5*chi(x_obs, x_model))


# 2c.) Caminata

# condiciones iniciales: tomen por ejemplo:
aini = 7.5
gammaini = 0.6
omegaini = 18.2

# numero de pasos: empiecen con 10000 y aumenten el número si ven que el
# algoritmo necesita mas pasos para converger.
iteraciones = 10000


def estimacionBayesiana(pasos, t, aini, gammaini, omegaini):
    arr_param = np.zeros((pasos, 4))

    a_old, gamma_old, omega_old = aini, gammaini, omegaini,
    x_old = model(t, a_old, gamma_old, omega_old)

    arr_param[0] = np.array([aini, gammaini, omegaini, 1])

    sigma1, sigma2, sigma3 = 0.1, 0.2, 0.3

    for i in range(1, pasos):
        x_old = model(t, a_old, gamma_old, omega_old)

        a_new = np.random.normal(a_old, sigma1)
        gamma_new = np.random.normal(gamma_old, sigma2)
        omega_new = np.random.normal(omega_old, sigma3)
        x_new = model(t, a_new, gamma_new, omega_new)

        alpha = verosimilitud(value_data_test, x_new) / \
            verosimilitud(value_data_test, x_old)

        if (alpha > 1):
            arr_param[i] = np.array([a_new, gamma_new, omega_new, alpha])
            a_old, gamma_old, omega_old = a_new, gamma_new, omega_new

        else:
            b = np.random.uniform(0, 1)
            if b < alpha:
                arr_param[i] = np.array([a_new, gamma_new, omega_new, alpha])

                a_old, gamma_old, omega_old = a_new, gamma_new, omega_new

            else:
                arr_param[i] = np.array([a_old, gamma_old, omega_old, alpha])
    return arr_param


estimacion = estimacionBayesiana(
    iteraciones, t_data_test, aini, gammaini, omegaini)

# 2d.) Seleccione los mejores parametros E IMPRIMA UN MENSAJE QUE DIGA:
# "LOS MEJORES PARAMETROS SON a=... gamma=... Y omega=..."

best_a = np.mean(estimacion[:, :1])
best_gamma = np.mean(estimacion[:, 1:2])
best_omega = np.mean(estimacion[:, 2:3])

print(
    f'los mejores parámetros son a= {best_a}, gamma={best_gamma}, omega={best_omega}')

# 2f.) Grafique sus datos originales y su modelo con los mejores parametros.
# Guarde su grafica sin mostrarla en Resorte.png

plt.figure()
f, ax = plt.subplots()
ax.plot(t_data, value_data, "g", label="Original data")
ax.plot(t_data, model(t_data, best_a, best_gamma, best_omega),
        "b--",  label="model with best parameters")
plt.legend()
plt.savefig("Resorte.png")
plt.close()

# 3) SABIENDO QUE omega=np.sqrt(k/m), imprima un mensaje dónde diga si puede
# o NO determinar k Y m de manera individual usando el método anterior.
# Justifique su respuesta (puede hacer pruebas con el código para responder).

# Revisemos si se puede refactorizar de tal modo que se pueda implementar los dos parámetos nuevos

# Definimos el nuevo modelo teniendo en cuenta estos neuvos parmámetros


def secondModel(t, a, gamma, k, m):
    omega = math.sqrt(k/m)
    return a*np.exp(-gamma*t)*np.cos(omega*t)


# Basados en que omegaini = 18.2, se define k y m como sigue:
kini = 33.124
mini = 0.1


def segundaEstimacionBayesiana(pasos, t, aini, gammaini, kini, mini):
    arr_param = np.zeros((pasos, 5))

    a_old, gamma_old, k_old, m_old = aini, gammaini, kini, mini
    x_old = secondModel(t, a_old, gamma_old,  k_old, m_old)

    arr_param[0] = np.array([aini, gammaini, kini, mini, 1])

    sigma1, sigma2, sigma3, sigma4 = 0.1, 0.15, 0.2, 0.25

    for i in range(1, pasos):
        x_old = secondModel(t, a_old, gamma_old,  k_old, m_old)

        a_new = np.random.normal(a_old, sigma1)
        gamma_new = np.random.normal(gamma_old, sigma2)
        k_new = abs(np.random.normal(k_old, sigma3))
        # Valor absoluto para evitar valores negativos
        m_new = abs(np.random.normal(m_old, sigma4))
        x_new = secondModel(t, a_new, gamma_new, k_new, m_new)

        alpha = verosimilitud(value_data_test, x_new) / \
            verosimilitud(value_data_test, x_old)

        if (alpha > 1):
            arr_param[i] = np.array([a_new, gamma_new, k_new, m_new, alpha])
            a_old, gamma_old, k_old, m_old = a_new, gamma_new, k_new, m_new

        else:
            b = np.random.uniform(0, 1)
            if b < alpha:
                arr_param[i] = np.array(
                    [a_new, gamma_new, k_new, m_new, alpha])

                a_old, gamma_old, k_old, m_old = a_new, gamma_new, k_new, m_new

            else:
                arr_param[i] = np.array(
                    [a_old, gamma_old, k_old, m_old, alpha])
    return arr_param


segundaEstimacion = segundaEstimacionBayesiana(
    iteraciones, t_data_test, aini, gammaini, kini, mini)

second_best_a = np.mean(segundaEstimacion[:, :1])
second_best_gamma = np.mean(segundaEstimacion[:, 1:2])
second_best_k = np.mean(segundaEstimacion[:, 2:3])
second_best_m = np.mean(segundaEstimacion[:, 3:4])


plt.figure()
f, ax = plt.subplots()
ax.plot(t_data, value_data, "g", label="Original data")
ax.plot(t_data, secondModel(t_data, second_best_a, second_best_gamma, second_best_k, second_best_m),
        "b--",  label="model with best parameters and k,m")
plt.legend()
plt.savefig("ResorteWithKandM.png")
plt.close()


print("\nEs posible como se ha podido ver, pero hay que tener cierto cuidado en varias cosas:")
print("Primero, Se debe escojer con cuidado k y m de tal forma que tenga sentido, y más si se planea reemplazar el valor de omegaini")
print("Segundo, que al calcular k_new y m_new, al usar np.random.normal existe la posibilidad de que los números sean negativos,")
print("por tanto se les tomó el valor absoluto")
print("Al ver la gráfica resultante, se ve que es una buena aproximación a los datos originales, aunque ha de verse que tan mejor es")
print("Comparada con solo usar Omega")

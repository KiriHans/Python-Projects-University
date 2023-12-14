import numpy as np
import matplotlib.pylab as plt



interval = np.arange(0, 2.00, 0.02 )

dataOnda = np.genfromtxt("ecuacion_de_onda_1.txt")

array = dataOnda[:, 1:]



sample = [0, 3.33333e-05, 0.0252333, 0.0585667, 0.0810333, 0.1]

for i in sample:
    array2 = dataOnda[:,1:][dataOnda[:, :1] == i]
    plt.figure()
    f, ax = plt.subplots()
    ax.plot(interval, array2 , "g", label="position")
    plt.legend()
    plt.savefig(f"ecuacion_de_onda_tiempo_{i}.png")
    plt.close()


# ecuacion_de_onda_2.txt
    

dataOnda2 = np.genfromtxt("ecuacion_de_onda_2.txt")
array = dataOnda2[:, 1:]

sample = [0, 0.0002, 0.0452]

for i in sample:
    array2 = dataOnda2[:,1:][dataOnda2[:, :1] == i]
    plt.figure()
    f, ax = plt.subplots()
    ax.plot(interval, array2 , "g", label="position")
    plt.legend()
    plt.savefig(f"ecuacion_de_onda_2_tiempo_{i}.png")
    plt.close()

    
# ecuación_de_onda_3.txt
    
dataOnda3 = np.genfromtxt("ecuacion_de_onda_3.txt")
array = dataOnda3[:, 1:]

sample = [0, 3.33333e-05, 0.0252333, 0.0585667, 0.0810333, 0.1]

for i in sample:
    array2 = dataOnda3[:,1:][dataOnda3[:, :1] == i]
    plt.figure()
    f, ax = plt.subplots()
    ax.plot(interval, array2 , "g", label="position")
    plt.legend()
    plt.savefig(f"ecuacion_de_onda_3_tiempo_{i}.png")
    plt.close()
    
    
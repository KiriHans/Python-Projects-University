import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, fft2, fftshift, ifft2

# Construcción de la señal
N = 128  # number of point in the whole interval
f = 200.0  # frequency in Hz
dt = 1 / (f * 32)  # 32 samples per unit frequency
t = np.linspace(0, (N-1)*dt, N)
y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi *
                                             (2*f) * t) + 0.17*np.sin(2 * np.pi * (15*f) * t)

# 1) implemente de la transformada de fourier discreta
n = np.arange(0, N, 1)
x = np.zeros(N, dtype=complex)
# n es un arreglo
for k in range(N):
    x[k] = np.sum(y*np.exp(-complex(0, 1)*2*np.pi*k*(n)/N))
print(x)

# 2) Genere el arreglo de las frecuencias (ver documentación de fftfreq):
n = t.size
timestep = dt
freq1 = np.fft.fftfreq(n, d=timestep)
print("freq1: ", freq1)
print("----")
# 3) Haga una gráfica comparando método propio con implementación de scipy.fftpack.fft
fft_x = fft(y)  # FFT
freq = fftfreq(n, dt)  # Recuperamos las frecuencias

fig, axs = plt.subplots(2, 1)
plt.sca(axs[0])
plt.plot(freq, (x*np.conj(x) / n), color="r", label="Sin funcion")
plt.legend()

plt.sca(axs[1])
plt.plot(freq, (fft_x*np.conj(fft_x) / n),
         color='b', label="Con funcion")
plt.legend()

plt.show()
plt.close()


# Ejercicio 2

# 1) Almacene los datos de signal.dat. La columna 1 es el tiempo y la columna 2 es su señal f(t).
# Grafique su señal en función del tiempo y guarde dicha gráfica sin mostrarla en signal.png.

signalTime = []
signal = []
for line in open("signal.dat", 'r'):
    signalTime.append(float(line.rsplit(",")[0].rstrip()))
    signal.append(float(line.rsplit(",")[1].rstrip()))

# Tamaño de la lista
n = len(signal)


# Transformación a numpy array
signalTime = np.array(signalTime)
signal = np.array(signal)

plt.figure()
plt.plot(signalTime, signal, 'r-')
plt.xlim(signalTime[0], signalTime[-1]) 
plt.savefig('signal.png')
plt.close()

# 2) Use fftfreq (BONO si usa su implementación propia) y haga una gráfica de su transformada de
# fourier en función de las frecuencias. Guarde dicha gráfica sin mostrarla en Fourier_trans.png

d = np.mean(signalTime)

if len(signal) % 2 == 0:
    f = np.append(np.arange(0, n//2, 1), np.arange(-n//2, 0, 1))/(n*d)
else:
    f = np.append(np.arange(0, (n-1)//2 + 1, 1),
                  np.arange(-(n-1)//2, 0, 1))/(n*d)


fft_x = fft(signal, n)  # FFT
PSD = fft_x * np.conj(fft_x) / n

plt.figure()
plt.plot(f, PSD)
plt.xlim(np.min(f), np.max(f))
plt.savefig("Fourier_trans.png")
plt.close()

# 3) Haga un filtro pasa bajos que le permita filtrar el ruido de la señal del punto 1. Use la gráfica de la
# transformada de fourier del punto 2 para determinar un valor apropiado de la frecuencia de corte que
# debe usar para filtrar dicho ruido de alta frecuencia.

indices = PSD > 5
PSDlimpio = PSD * indices
fft_x = fft_x * indices
ifft_x = np.fft.ifft(fft_x)


plt.figure
plt.plot(signalTime, signal,
         color='b', label="Con ruido")
plt.legend()


plt.plot(signalTime, ifft_x, color="r", label="Limpio")
plt.legend()

plt.savefig("clean_signal_vs_noise.png")
plt.close()

# Ejercicio 4


# 1) Almacene los datos de la imagen (use imread:
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html)

im = plt.imread("NASA_Moon.jpg")


# 2) Use la librería de scipy de transformada de fourier en 2d y la trasnformada inversa
# (https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.fft2.html) para hacer un código que filtre el
# ruido periodico que tiene la imagen de la luna.
fft2_im = fftshift(fft2(im))
PSD = abs(fft2_im)


indices1 = PSD < 9*10**(4)
indices2 = 10**(4) < PSD

PSD[347:353, :560] = PSD[347:353, :560] * indices1[347:353, :560]
PSD[347:353, 640:] = PSD[347:353, 640:] * indices1[347:353, 640:]


fft2_im[347:353, :560] = fft2_im[347:353, :560] * indices1[347:353, :560]
fft2_im[347:353, 640:] = fft2_im[347:353, 640:] * indices1[347:353, 640:]


ifft2_im = ifft2(fft2_im)


# 3) haga una gráfica de la imagen filtrada y guárdela en LunaFiltrada.png

plt.imshow(abs(ifft2_im), plt.cm.gray)
plt.savefig('LunaFiltrada.png')
plt.close('all')

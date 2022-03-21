import numpy as np
import matplotlib.pyplot as plt


# Funkcja numer 8

# Parametr f - częstość próbkowania
f = 2

T = 1 / f

# Częstotliwość próbkowania
fs = 8000

# Okres próbkowania
Ts = 1/fs

# Czas trwania sygnału
Tc = 1

# Liczba próbek przypadających na cały sygnał
N = Tc * fs

# Wartość fi
fi = 2 * np.pi

t = np.arange(0, (N - 1) / fs, Ts)

# Funkcja
x = (1 - t) * np.sin(2 * np.pi * f * t + fi) * np.cos(4 * np.pi * t)

plt.plot(t, x, label='x(t)')
plt.title('Zad 1')
plt.savefig('TD-Lab2_Zad1.png')
plt.show()

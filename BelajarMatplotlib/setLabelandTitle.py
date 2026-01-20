import os
import numpy as np
import matplotlib.pyplot as plt
os.system("cls")

# 1. Membuat data (sin(2wt + theta))
def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)                       # Membuat array waktu dari 0 sampai tAkhir dengan step 0.1
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))  # Menghitung nilai sinus dengan fase theta (diubah ke radian)
    return t, y                                         # Mengembalikan array waktu dan nilai sinus

amplitudo = 1                                           # Amplitudo gelombang
frekuensi = 1                                           # Frekuensi gelombang
theta = 0                                               # Fase awal gelombang
tAkhir = 4                                             # Batas waktu simulasi

t, y = sinusGenerator(amplitudo, frekuensi, tAkhir, theta)  # Memanggil fungsi untuk membuat data gelombang

# 2. Membuat plot
plt.plot(t, y)                                         # Menggambar grafik sinusoidal

# 2.1 Membuat label dan title
judul = 'Grafik Sinusoidal\n'                           # Judul utama grafik
rumus = r'$ \mathcal{Y} = A.sin(2 \omega t +\theta) $' + '\n'  # Menambahkan rumus matematika dalam LaTeX
parameter1 = r'$ A = $' + str(amplitudo) + 'cm, '     # Menambahkan parameter amplitudo
parameter2 = r'$ \omega =  $' + str(frekuensi) + r'$ \mathit{Hz} $' + ', '  # Menambahkan parameter frekuensi
parameter3 = r'$ \theta =  $' + str(theta) + r'$ ^{0} $'  # Menambahkan parameter fase

plt.title(judul + rumus + parameter1 + parameter2 + parameter3)  # Menampilkan judul lengkap dengan rumus dan parameter
plt.xlabel('waktu(detik)')                             # Label sumbu X
plt.ylabel('magnituda(cm)')                             # Label sumbu Y

# 3. Menampilkan plot
plt.show()                                             # Menampilkan jendela grafik

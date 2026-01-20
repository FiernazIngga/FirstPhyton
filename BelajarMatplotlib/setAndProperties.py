import os
import numpy as np
import matplotlib.pyplot as plt

os.system("cls")

# 1. Membuat data (sin(2wt + theta))
def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)                       # Membuat array waktu dari 0 sampai tAkhir dengan step 0.1
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))  # Menghitung nilai sinus dengan fase theta (diubah ke radian)
    return t, y                                         # Mengembalikan array waktu dan nilai sinus

t1, y1 = sinusGenerator(1, 1, 4, 0)                    # Membuat data untuk fase 0°
t2, y2 = sinusGenerator(1, 1, 4, 90)                   # Membuat data untuk fase 90°
t3, y3 = sinusGenerator(1, 1, 4, 180)                  # Membuat data untuk fase 180°

# 2. Membuat plot
dataPlot1 = plt.plot(t1, y1)                           # Plot data fase 0°
dataPlot2 = plt.plot(t2, y2)                           # Plot data fase 90°
dataPlot3 = plt.plot(t3, y3)                           # Plot data fase 180°

# 2.1 Setting properties
plt.setp(dataPlot1, color='r', linestyle='-', linewidth=0.75)   # Atur warna merah, garis solid tipis untuk fase 0°
plt.setp(dataPlot2, color='b', linestyle='-.', linewidth=4)     # Atur warna biru, garis putus-titik tebal untuk fase 90°
plt.setp(dataPlot3, color='g', linestyle='--', linewidth=1.25)  # Atur warna hijau, garis putus-putus sedang untuk fase 180°

# 3. Menampilkan plot
plt.show()                                             # Menampilkan jendela grafik

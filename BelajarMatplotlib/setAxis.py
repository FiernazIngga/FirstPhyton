import os
import numpy as np
import matplotlib.pyplot as plt
os.system("cls")

# 1. Membuat data (sin(2wt + theta))
def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)                       # Membuat array waktu dari 0 sampai tAkhir dengan step 0.1
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))  # Menghitung nilai sinus dengan fase theta (diubah ke radian)
    return t, y                                         # Mengembalikan array waktu dan nilai sinus

t, y = sinusGenerator(1, 1, 4, 0)                       # Memanggil fungsi untuk membuat data gelombang

# 2. Membuat plot
plt.plot(t, y)                                         # Menggambar grafik sinusoidal

# 2.1 Setting axis, minimum dan maximum
# plt.axis([xmin, xmax, ymin, ymax])
plt.axis([0, 4, -2, 2])                                # Menentukan batas sumbu X dari 0–4 dan sumbu Y dari -2–2

# 3. Menampilkan plot
plt.show()                                             # Menampilkan jendela grafik

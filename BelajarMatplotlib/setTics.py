import os
import numpy as np
import matplotlib.pyplot as plt
os.system("cls")

# 1. Membuat data (sin(2wt + theta))
sudut = np.arange(0,360,1)             # Membuat array sudut dari 0 sampai 359 derajat (step 1 derajat)
y = np.sin(np.deg2rad(sudut))          # Menghitung nilai sinus dari sudut (dikonversi ke radian)

# 2. Membuat plot
plt.plot(sudut, y)                     # Menggambar grafik sinus dengan sumbu-x = sudut, sumbu-y = nilai sinus
plt.ylabel('Magnituda')                # Memberi label pada sumbu Y
plt.xlabel('Sudut')                    # Memberi label pada sumbu X

plt.yticks([-1,0,1])                   # Menentukan nilai yang muncul di sumbu Y
plt.xticks(
    [0, 90, 180, 270, 360],           # Posisi tick pada sumbu X (derajat)
    [r'$ {0^o} $', r'$ {90^o} $', r'$ {180^o} $', r'$ {270^o} $', r'$ {360^o} $']  # Label tick dengan LaTeX
)

# 3. Menampilkan plot
plt.show()                             # Menampilkan jendela grafik

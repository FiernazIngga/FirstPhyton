import os                      
import numpy as np            
import matplotlib.pyplot as plt  

os.system("cls")            

# 1. MEMBUAT DATA SINUS
sudut = np.arange(0, 360, 1)   # Membuat array sudut dari 0 sampai 359 derajat (step 1 derajat)
y = np.sin(np.deg2rad(sudut))  # Menghitung nilai sinus dari sudut (diubah ke radian)

# 2. MEMBUAT PLOT
plt.plot(sudut, y)             # Menggambar grafik sinus dengan sumbu-x = sudut, sumbu-y = nilai sinus

# 3. MENAMBAHKAN TEKS DI GRAFIK
plt.text(190, 1, 'Magnituda')  # Menambahkan teks "Magnituda" di posisi (x=190, y=1)
plt.text(360, 0.05, 'Sudut')  # Menambahkan teks "Sudut" di posisi (x=360, y≈0)

# 4. MENGATUR TICK PADA SUMBU Y
plt.yticks(
    [-1, -0.5, 0, 0.5, 1]      # Menentukan nilai yang muncul di sumbu Y
)

# 5. MENGATUR TICK & LABEL SUMBU X
plt.xticks(
    [0, 90, 180, 270, 360],    # Posisi tick pada sumbu X (derajat)
    [
        r'$ {0^o} $',          # Label 0 derajat (pakai LaTeX supaya rapi)
        r'$ {90^o} $',
        r'$ {180^o} $',
        r'$ {270^o} $',
        r'$ {360^o} $'
    ]
)

# 6. MENGAKSES AXES (TULANG GRAFIK)
ax = plt.gca() # gca = Get Current Axes (mengambil axes aktif)
ax.spines['left'].set_position(('data', 180)) # Menggeser garis sumbu Y ke posisi x = 180
ax.spines['bottom'].set_position(('data', 0)) # Menggeser garis sumbu X ke posisi y = 0
ax.spines['right'].set_color('none') # Menghilangkan garis sumbu kanan
ax.spines['top'].set_color('none') # Menghilangkan garis sumbu atas

# 7. MENAMPILKAN GRAFIK
plt.show()

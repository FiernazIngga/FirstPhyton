import os
import numpy as np
import matplotlib.pyplot as plt
os.system("cls")

# 1. Membuat data (sin(2wt + theta))
def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)                       # Membuat array waktu dari 0 sampai tAkhir dengan step 0.1
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))  # Menghitung nilai sinus dengan fase theta (diubah ke radian)
    return t, y                                         # Mengembalikan array waktu dan nilai sinus

# 2. Membuat plot
t1, y1 = sinusGenerator(1, 1, 4, 0)
plt.plot(t1, y1)                                       # Plot garis default untuk fase 0°

t2, y2 = sinusGenerator(1, 1, 4, 30)
plt.plot(t2, y2, 'r')                                  # Plot garis merah untuk fase 30°

t3, y3 = sinusGenerator(1, 1, 4, 60)
plt.plot(t3, y3, 'b--')                                # Plot garis biru putus-putus untuk fase 60°

t4, y4 = sinusGenerator(1, 1, 4, 90)
plt.plot(t4, y4, 'b-o')                                # Plot garis biru dengan marker lingkaran (-o-) untuk fase 90°

# 3. Menampilkan plot
plt.show()                                             # Menampilkan jendela grafik

# Keterangan simbol marker di matplotlib:
# "."   point
# ","   pixel
# "o"   circle
# "v"   triangle_down
# "^"   triangle_up
# "<"   triangle_left
# ">"   triangle_right
# "1"   tri_down
# "2"   tri_up
# "3"   tri_left
# "4"   tri_right
# "8"   octagon
# "s"   square
# "p"   pentagon
# "P"   plus (filled)
# "*"   star
# "h"   hexagon1
# "H"   hexagon2
# "+"   plus
# "x"   x
# "X"   x (filled)
# "D"   diamond
# "d"   thin_diamond
# "|"   vline
# "_"   hline

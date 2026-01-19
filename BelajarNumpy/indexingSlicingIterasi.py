import os
import numpy as np
os.system("cls")

a = np.arange(10)**2

print(a)

# Mengambil nilai
print("Elemen ke 1 dari a adalah ", a[0])
print("Elemen terakhir dari a adalah ", a[-1])
print()

# Slicing
print("Elemen dari 1 - 6 adalah ", a[0:6]) # [start, end]
print("Elemen dari 4 sampai akhir adalah ", a[3:]) 
print("Elemen dari awal sampai 5 adalah ", a[:5]) 
print()

# Iterasi
for i in a:
    print("Value = ", i)
print()
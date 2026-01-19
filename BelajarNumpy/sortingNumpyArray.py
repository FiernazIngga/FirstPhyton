import os
import numpy as np
os.system("cls")

a = np.floor(np.random.randn(1,6)*10) # Membuat array 1 Dimensi berisikan random

print("Array asli: ", a)
print()

print("Nilai maks dari a: ", a.max())
print("Posisi max dari a = ", a.argmax())
print("Nilai min dari a: ", a.min())
print("Posisi min dari a = ", a.argmin())
print()

print("Mengurutkan nilai dari a: ")
print(np.sort(a))
print("Mengurutkan nilai dari arg a (Mengurutkan letak index dari urutan nilai a): ")
print(np.argsort(a))
print()

a2 = np.floor(np.random.randn(2,2)*10) # Membuat array 2 Dimensi berisikan random

print("Array asli: ")
print(a2)
print()

print("Nilai maks dari a: ", a2.max())
print("Posisi max dari a = ", a2.argmax())
print("Nilai min dari a: ", a2.min())
print("Posisi min dari a = ", a2.argmin())
print()

print("Mengurutkan nilai dari a: ")
print(np.sort(a2))
print("Mengurutkan nilai dari arg a (Mengurutkan letak index dari urutan nilai a): ")
print(np.argsort(a2))
print()

dtipe = [('nama','S10'),('tinggi',int)]
data = [
    ("Ucup",170),
    ("Otong", 150),
    ("Mario",160)
]

a3 = np.array(data, dtype=dtipe)
print(a3)
print()

print(np.sort(a3, order='tinggi'))
print(np.sort(a3, order='nama'))
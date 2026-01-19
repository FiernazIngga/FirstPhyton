import os
import numpy as np
os.system("cls")

# Membuat matrix dengan tipe data tertentu
a = np.array(([1,2,3],[3,4,5]), dtype=float)

# Membuat matrix dengan menggunakan function
def kuadrat(baris, kolom):
    return kolom**2

def jumlahBarisDanKolom(baris, kolom):
    return kolom + baris

b = np.fromfunction(kuadrat, (1,10), dtype=int)
c = np.fromfunction(jumlahBarisDanKolom, (4,4), dtype=float)

# Membuat array atau matrix dengan menggunakan iterasi
iterable = (x**2 for x in range(5))
d = np.fromiter(iterable, dtype=int)

# Multitipe array
dtipe = [("nama", "S225"),("tinggi", int)]

data = [
    ("Ucup",150),
    ("Otong",160),
    ("Mario",180)
]

e = np.array(data, dtype=dtipe)
print(e[0])
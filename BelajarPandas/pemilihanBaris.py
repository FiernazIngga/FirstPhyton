import pandas as pd
import numpy as np
import os
os.system('cls')

# Membuat sebuah tabel
baris = 10
kolom = 5
namaKolom = tuple('ABCDE')
df = pd.DataFrame(np.random.randint(1,5,size=(baris, kolom)), columns=namaKolom) # Mengacak isian angka 1 sampai 5

# Asli dari isin adalah df = df[(df['A']==1)|(df['A']==3)]
hanya1dan3 = df[df['A'].isin([1,3])] # Mengambil isian dari baris A dengan isian hanya 1 atau 3
selain1dan3 = df[~df['A'].isin([1,3])] # Mengambil isian dari baris A dengan isian bukan 1 atau 3

print(selain1dan3)
import os
os.system("cls")

import matematika as math # <- bisa pakai semua

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as p

hasilTambah = add(1,2,3,4,5)
print(f"Hasil tambah = {hasilTambah}")

hasilKali = math.kali(1,2,3,4,5)
print(f"Hasil kali = {hasilKali}")

pangkat_3 = p(3)
print(f"Hasil pangkat = {pangkat_3(3)}")
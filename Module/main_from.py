import os
os.system("cls")

from matematika import tambah, kali, pangkat
# from matematika import * Mengambil semua tanpa perlu pake satu satu kayak diatasnya

hasilTambah = tambah(1,2,3,4,5)
print(f"Hasil tambah = {hasilTambah}")

hasilKali = kali(1,2,3,4,5)
print(f"Hasil kali = {hasilKali}")

pangkat_3 = pangkat(3)
print(f"Hasil pangkat = {pangkat_3(3)}")
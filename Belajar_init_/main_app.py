import os
os.system("cls")

import sains
from sains.matematika import saintific # untuk yang saintific

hasilTambah = sains.matematika.tambah(1,2,3,4,5)
print(f"Hasil tambah = {hasilTambah}")
print()

hasilGaya = sains.fisika.gaya(10,9.8)
print(f"Hasil gaya = {hasilGaya}")
print()

hasilKali = sains.matematika.kali(1,2,3,4,5)
print(f"Hasil kali = {hasilKali}")
print()

hasilPangkat = saintific.pangkat(3)
print(f"Hasil pangkat = {hasilPangkat(2)}")
print()

# from sains import *

# hasilTambah = matematika.basic.tambah(1,2,3,4,5)
# print(f"Hasil tambah = {hasilTambah}")
# print()

# hasilGaya = fisika.gaya(10,9.8)
# print(f"Hasil gaya = {hasilGaya}")
# print()

# hasilKali = matematika.basic.kali(1,2,3,4,5)
# print(f"Hasil kali = {hasilKali}")
# print()
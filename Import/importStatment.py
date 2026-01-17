import os
os.system("cls")

# Import fungsinya adalah untuk mengambil program dari file external .py

# 1. untuk menyambung program dari external
import programPrint
import programNama

# 2. import dengan data
import variable

# data ada di namespace variable
print(variable.data)

# 3. Import dengan fungsi
import matematika
hasil = matematika.tambah(4,5)
print(hasil)
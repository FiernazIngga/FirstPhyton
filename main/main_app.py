import os
os.system("cls")

# __name__ = "__main__"

## __name__ pada file program utama
print(f"nilai __name__ pada main.py = '{__name__}'")

import fungsi

## contoh penggunaan __main__

# deklarasi
def fungsiTambah(a, b):
    return a + b

# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsiTambah(angka1,angka2)
    print(f"hasil tambah = {hasil}")

# import package
import package
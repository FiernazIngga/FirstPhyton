import os
os.system("cls")

nama_global = "Otong" # Variable global

# Akses variable global dalam fungsi
def fungsi1():
    print(f"Fungsi menampilkan {nama_global}")

fungsi1()
print()

# Akses variable global dalam fungsi
for i in range(5):
    print(f"Loop ke-{i} - {nama_global}")
print()

# Percabangan
if True:
    print(f"If menampilkan variable global {nama_global}")
print()

## Variable local scope
def fungsi2():
    print(f"Hello {nama}")

nama = "Otong" 
fungsi2()
print()

angka = 0 # Variable nya yang global disini
def ubahAngka(nilai_baru):
    global angka # Agar ini menggunakan variable global
    angka = nilai_baru

print(f"Sebelum {angka}")
ubahAngka(10)
print(f"Sesudah {angka}")
print()

# Contoh lain
angka = 0

for i in range(0,5):
    angka += i
    angkaDummy = 0

print(angka)
print(angkaDummy)
print()

if True:
    angka = 10
    angkaDummy = 10

print(angka)
print(angkaDummy)
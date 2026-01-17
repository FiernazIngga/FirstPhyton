import os
os.system('cls')

def fungsiKuadrat(inputAngka):
    output = inputAngka**2
    return output

def fungsiTambah(angka1, angka2):
    return angka1 + angka2

def operasiMtk(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah, kurang, kali, bagi

print(fungsiKuadrat(5))
print(fungsiTambah(10,5))
tambah, kurang, kali, bagi = operasiMtk(9,5)
print(f"Hasil tambah = {tambah}")
print(f"Hasil kurang = {kurang}")
print(f"Hasil kali = {kali}")
print(f"Hasil bagi = {tambah}")


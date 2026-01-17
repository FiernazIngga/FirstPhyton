import os
os.system("cls")

# kenalan dengan *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dengan berat {berat}")

fungsi("Dudung", 120, 120)

# Studi kasus

def tambah(*data):
    output = 0
    for angka in data:
        output += angka
    return output

hasil = tambah(1,2,3,4,5,6,7)
print(hasil)
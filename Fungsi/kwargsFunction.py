import os
os.system("cls")

def fungsi(**kwargs):
    print(kwargs)

fungsi(nama = "Ucup", tinggi = 183, berat = 79)

def fungsi(**kwargs):
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f"{nama} punya tinggi {tinggi} dengan berat {berat}")

fungsi(nama = "Ucup", tinggi = 183, berat = 79)
print()

# Studi kasus

def math(*args, **kwargs):
    hasil = 0
    if kwargs['option'] == "tambah":
        for angka in args:
            hasil += angka
    elif kwargs['option'] == "kali":
        hasil = 1
        for angka in args:
            hasil *= angka
    else:
        print("Tidak cocok")
    return hasil

hasil = math(1,2,3,4,5, option = "kali")
print(hasil)
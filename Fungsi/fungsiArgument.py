import os
os.system('cls')

def hello_world(nama):
    print(f"Selamat datang wahai {nama}")
    print()

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
    print()

def say_hi(listPeserta):
    dataPeserta = listPeserta.copy()
    for peserta in dataPeserta:
        print(f"Yang terhormat {peserta}")
    print()

hello_world("Ucup")
tambah(10,12)
anggota = ["Ucup", "Otong", "Dudung"]
say_hi(anggota)
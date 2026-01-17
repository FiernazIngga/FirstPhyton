import os
os.system('cls')

def sayHelo(nama = "Guest"):
    print(f"Hallo {nama}")

def sapaDia(nama, pesan = "Apa kabar"):
    print(f"Hai {nama}, {pesan}")

def hitungPangkat(angka, pangkat = 2):
    hasil = angka**pangkat
    return hasil

sayHelo("Ucup")
sayHelo()
sapaDia("Ucup", "Hai bro")
sapaDia("Hola")
print(hitungPangkat(pangkat = 3, angka = 5))

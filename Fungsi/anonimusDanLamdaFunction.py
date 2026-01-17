import os
os.system("cls")

def kudrat(angka):
    return angka**2

print(f"Hasil fungsi kuadrat = {kudrat(3)}")
print()

## Kita coba dengan lambda
# output = lamda argument: expression
kuadratLambda = lambda angka:angka**2
print(f"Hasil kuadrat lambda adalah = {kuadratLambda(3)}")
print()

pangkat = lambda num, pow: num**pow
print(f"Hasil lambda pangkat = {pangkat(4,2)}")
print()

## Kegunaannya
# sorting biasa untuk list
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort()
print(f"Sorted list = {data_list}")
print()

# sorting dia pakai jumlah karakter
def panjangNama(nama):
    return len(nama)

data_list.sort(key=panjangNama)
print(f"Sorted list by panjang = {data_list}")
print()

# Sort pakai lambda
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort(key=lambda nama:len(nama))
print(f"Sorted list by lambda = {data_list}")
print()

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
data_angka_baru = list(filter(lambda angka: angka<5, data_angka))
print(f"Pilih angka by lambda = {data_angka_baru}")
print()

# kasus genap
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
data_angka_baru = list(filter(lambda angka: angka%2==0, data_angka))
print(f"Pilih genap angka by lambda = {data_angka_baru}")
print()

# kasus ganjil
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
data_angka_baru = list(filter(lambda angka: angka%2!=0, data_angka))
print(f"Pilih ganjil angka by lambda = {data_angka_baru}")
print()

# Kelipatan tiga
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
data_angka_baru = list(filter(lambda angka: angka%3==0, data_angka))
print(f"Pilih angka kelipatan 3 by lambda = {data_angka_baru}")
print()

## Anonymous function
# currying <- Haskell Curry

def pangkat(angka, n):
    hasil = angka**n
    return hasil

print(f"Hasil pangkat = {pangkat(5,2)}")
print()

# dengan currying
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2) 
print(f"Pangkat 2 = {pangkat2(5)}")
print()

pangkat3 = pangkat(3) 
print(f"Pangkat 3 = {pangkat3(5)}")
print()

print(f"Pangkat bebas = {pangkat(2)(5)}")
print()
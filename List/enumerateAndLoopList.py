import os
os.system('cls')

## Looping dari list

# for loop
kumpulanAngka = [4,3,2,5,6,1]
for angka in kumpulanAngka:
    print(f"Angka = {angka}")
print("\n")

peserta = ["Ucup", "Otong", "Dadang", "Diding"]
for nama in peserta:
    print(f"Nama = {nama}")
print("\n")

# for loop dan range
kumpulanAngka2 = [10,5,4,2,6,5]
panjang = len(kumpulanAngka2)
for i in range(panjang):
    print(f"Angka = {kumpulanAngka2[i]}")
print("\n")

# While
kumpulanAngka2 = [10,5,4,2,6,5]
panjang = len(kumpulanAngka2)
i = 0
while i < panjang:
    print(f"Angka = {kumpulanAngka2[i]}")
    i+=1
print("\n")

# List comprehension
data = ["Ucup",1,2,3,"Otong"]
[print(f"data = {i}") for i in data]
print("\n")

# Enumerate
dataList = ["Ucup",1,2,3,"Otong"]
for index, data in enumerate(dataList):
    print(f"Index = {index}, Data = {data}")
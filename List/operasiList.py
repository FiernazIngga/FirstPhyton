import os
os.system('cls')

dataAngka = [1,2,4,2,7,4,6,9,32,1,4,6,3,8,3,2,5,7,5,3,5,2]
print(f"Data angka = \n{dataAngka}\n")

# Count data

jumlah_data_2 = dataAngka.count(2)
jumlah_data_3 = dataAngka.count(3)

print(f"Jumlah angka 2 = {jumlah_data_2}\n")
print(f"Jumlah angka 3 = {jumlah_data_3}\n")



### Ambil posisi data

data = ["Ucup", "Otong", "Dudung", "Ujang"]
print(f"Data nama = \n{data}\n")

# Ambil indeks
indexDudung = data.index("Dudung")
print(f"Index si Dudung = {indexDudung}\n")

# Mengurutkan list
print(f"Data angka sebelum short = \n{dataAngka}\n")
dataAngka.sort()
print(f"Data angka sesudah short = \n{dataAngka}\n")

print(f"Data nama sebelum short = \n{data}\n")
data.sort()
print(f"Data angka sesudah short = \n{data}\n")

# Balik list 
dataAngka.reverse()
print(f"Data angka sesudah reverse = \n{dataAngka}\n")
data.reverse()
print(f"Data angka sesudah reverse = \n{data}\n")

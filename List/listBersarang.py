import os
os.system('cls')

data_0 = [1,2]
data_1 = [3,4]

list2D = [data_0, data_1]
print(f"Data 2D = \n{list2D}\n")

# Contoh penggunaan
peserta_0 = ["Ucup", 25, "Laki-laki"]
peserta_1 = ["Otong", 10, "Laki-laki"]
peserta_2 = ["Dedeh", 30, "Wanita"]

listPeserta = [peserta_0, peserta_1, peserta_2]
print(f"List peserta = \n{listPeserta}\n")

for peserta in listPeserta:
    print(f"Nama   : {peserta[0]}")
    print(f"Umur   : {peserta[1]}")
    print(f"Gender : {peserta[2]}\n")

# Reference
listCopy = listPeserta.copy()
print(f"List peserta = \n{listCopy}\n")
peserta_0[0] = "Michael"
print(f"List peserta awal = \n{listPeserta}\n")
print(f"List peserta copy = \n{listCopy}\n")

import os
os.system('cls')

# Index  0 (-3)  1 (-2)   2 kalau dari belakang (-1)
data = ["Ucup", "Otong", "Dudung"]

## Mengambil data dari list ini
print(f"Data pertama (Index 0)                = {data[0]}")
print(f"Data pertama dari belakang (Index -3) = {data[-3]}")

# Mengambil info jumlah data
panjangData = len(data)
print(f"Panjang data adalah {panjangData}")

## Manipulasi data list

print(f"\nData sebelum ditambah = \n{data}\n")

# Menambah item pada list
data.insert(1, "Asep") # Menambahkan data berdasarkan angka 1 yaitu index 1
print(f"Data sesudah ditambah di indeks ke 1 = \n{data}\n")


# Menambah data di akhir
data.append("Jajang")
print(f"Data ditambah diakhir = \n{data}\n")

# Menambahkan list dengan list
dataBaru = ["Ujang", "Usep", "Dadang"]
data.extend(dataBaru) # Menambah data ditambah data baru
print(f"Data gabungan = \n{data}\n")

# Merubah data
for index, isi in enumerate(data):
    if isi == "Otong":
        data[index] = "Michael"
print(f"Data diubah = \n{data}\n")

# Menghilangkan data
while "Ucup" in data:
    data.remove("Ucup")
print(f"Data hapus = \n{data}\n")

# Meremove data paling belakang
dataAkhir = data.pop()
print(f"Data hapus paling belakang = \n{data}\n")
print(f"Data yang dihapus = {dataAkhir}\n")
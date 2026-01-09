import os
os.system('cls')

# Ini dengan list
angka = [0,1,2,3,4]
print(angka)
for i in angka: # 
    print(f"i sekarang -> {i}")
print("Ini adalah akhir dari program 1\n")

# Ini dengan range
angka_range = range(5)
for i in angka_range: # Sama kayak pakai for i in range(5):
    print(f"i sekarang -> {i}")
print("Ini adalah akhir dari program 2\n")

# Ini dengan range batasan
angka_range2 = range(1,5) # Artinya mulai dari 1 diakhiri sampai 4, ga 5 karena kayak array dimulai dari 0
for i in angka_range2: # Sama kayak pakai for i in range(5):
    print(f"i sekarang -> {i}")
print("Ini adalah akhir dari program 3\n")

# Menggunakan string
data_str = "Saya ganteng abis"
for huruf in data_str:
    print(huruf)
print("Ini adalah akhir dari program 4\n")

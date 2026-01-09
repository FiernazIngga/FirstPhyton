import os
os.system('cls')

# Pertama perkenalan
angka = 0
while angka < 5:
    print(f"Angka sekarang -> {angka}")
    angka+=2
    print("Telah ditambah 2")
    if (angka > 5):
        print(f"Angka sekarang -> {angka}, ini sudah diluar perulangan jadi paling akhir\n")
    else:
        print(f"Angka sekarang -> {angka}\n")
print("Program 1 berakhir\n")
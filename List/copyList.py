import os
os.system('cls')

## Teknik menduplikasikan list

a = ["Ucup", "Otong", "Dudung"]
print(f"a = {a}\n")

b = a
print(f"b = {b}\n")

# Kita akan merubah member dari a

# Akan merubah kedua list
a[1] = "Michael"
b.sort()

print(f"a = {a}\n")
print(f"b = {b}\n")

# Memori dari kedua list
print(f"Address a = {hex(id(a))}\n")
print(f"Address b = {hex(id(b))}\n")

# Melakukan duplikasi atau copy 
print("Membuat list c dengan a.copy()\n")
c = a.copy()
print(f"Address a = {hex(id(a))}\n")
print(f"Address b = {hex(id(b))}\n")
print(f"Address c = {hex(id(c))}\n")

c[0] = "Dadang"
print(f"a = {a}\n")
print(f"c = {c}\n")

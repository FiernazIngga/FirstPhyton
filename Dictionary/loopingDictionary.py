import os
os.system('cls')

temanDict = {
    "cup": "Ucup Surucup",
    "tong": "Otong surotong",
    "dung": "Dudung surudung",
    "sep": "Aseep Sikasep",
    "cuy": "Ucuy surucuy"
}

# Looping first try
for teman in temanDict: # Yang keluar ada key nya
    print(teman)
print()

# Operator untuk mengambil item / iterable
keys = temanDict.keys() # Munculin key nya
print(keys)
for key in temanDict.keys():
    print(temanDict.get(key))
print()

values = temanDict.values() # Munculin valuesnya 
print(values)
for value in temanDict.values():
    print(value)
print()

items = temanDict.items() # Munculin key dan valuenya 
print(items)
for item in temanDict.items():
    print(item)
print()
for key,value in temanDict.items():
    print(f"{key}, value = {value}")
print()
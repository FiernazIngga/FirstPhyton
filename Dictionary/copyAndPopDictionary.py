import os
os.system('cls')

teman_teman = {
    "cup": "Ucup Surucup",
    "tong": "Otong surotong",
    "dung": "Dudung surudung",
    "sep": "Aseep Sikasep",
    "cuy": "Ucuy surucuy"
}

friends = teman_teman.copy()
print(f"teman_teman: \n{teman_teman}\n")
print(f"friends: \n{friends}\n")

teman_teman['cup'] = "Cup Cracki"

print(f"teman_teman: \n{teman_teman}\n")
print(f"friends: \n{friends}\n")

# pop dictionary
dataAsep = friends.pop('sep')
print(f"Ini adalah data asep: {dataAsep}")
print(f"friends: {friends}\n")

# Pop item dictionary
dataTerakhir = friends.popitem()
print(f"Data terakhir: {dataTerakhir}")
print(f"friends: {friends}\n")

import os
import datetime
os.system('cls')

mahasiswa1 = {
    "nama":"Ucup Surucup",
    "nim": "001",
    "sks_lulus": 130,
    "beasiswa": False,
    "lahir": datetime.datetime(2001,4,10)
}

mahasiswa2 = {
    "nama":"Otong Surotong",
    "nim": "002",
    "sks_lulus": 140,
    "beasiswa": True,
    "lahir": datetime.datetime(2002,10,10)
}

mahasiswa3 = {
    "nama":"Asep Kasep",
    "nim": "003",
    "sks_lulus": 100,
    "beasiswa": False,
    "lahir": datetime.datetime(1999,5,11)
}

data_mahasiswa = {
    "mhs1": mahasiswa1,
    "mhs2": mahasiswa2,
    "mhs3": mahasiswa3
}

print(f"{'KEY':^4} {'Nama':^17} {'Nim':^4} {'SKS':^3} {'Beasiswa':^9} {'Lahir':^10}")
print("-"*54)

for mahasiswa in data_mahasiswa:
    key = mahasiswa
    nama = data_mahasiswa[key]['nama']
    nim = data_mahasiswa[key]['nim']
    sks_lulus = data_mahasiswa[key]['sks_lulus']
    beasiswa = data_mahasiswa[key]['beasiswa']
    lahir = data_mahasiswa[key]['lahir'].strftime("%x")
    print(f"{key:^4} {nama:^17} {nim:^4} {sks_lulus:^3} {beasiswa:^9} {lahir:^10}")
    print("-"*54)
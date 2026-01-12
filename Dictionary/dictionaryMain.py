import os
os.system('cls')

## Dictionary (dict) -> associative array
# identifier -> key

# dataDict = {
#     'cp': 'Ucup',
#     'tg': 'Otong',
#     'dg': 'Dudug'
# }

# print(dataDict['cp'])

## Operator Dictionary 

dataDict = {
    "cup": "Ucup Surucup",
    "tong": "Otong Surotong",
    "dung": "Dudung Surudung",
}

# Panjang dictionary
lendict = len(dataDict)
print(f"Panjang dari dict {lendict}\n")

# Mengecek key ada atau tidak
key = "kis"
cekKey = key in dataDict
print(f"Cek apakah {key} ada di dataDict: {cekKey}\n")

# Mengakses value (read) dengan get
print(dataDict['cup']) # Kalau ini program akan error kalau key ga ada
print(dataDict.get('cup'))
print(dataDict.get('kis')) # Muncul none
print()

# Mengupdate data
dataDict['cup'] = "Ucup si ganteng"
print(dataDict['cup'])
dataDict['sep'] = "Asep si kasyep"
print(dataDict)
dataDict.update({"cup": "Ucup Surucup"})
print(dataDict)
dataDict.update({"faqih": "Faqihya"}) # Fungsi update tuh kalo ada keynya maka update, kalau ga ada di tambah
print(dataDict)
print()

# Mendelete data pada dictionary
del dataDict['faqih']
print(dataDict)
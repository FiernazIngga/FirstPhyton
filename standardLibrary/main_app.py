import os
os.system("cls")

import datetime
data_waktu = datetime.datetime.now()
print(f"Datetime now : {data_waktu}")
print(f"Tahun : {data_waktu.year}")
print(f"Hari : {data_waktu.strftime('%A')}")
print()

from collections import Counter
data = ["a","b","c","d","a","d","e"]
dataCount = Counter(data)
print(f"Data count = {dataCount}")
print(f"Jumlah a = {dataCount['a']}")
print()

import io
file = io.open("standardLibrary/file_text.txt","r")
print(file.read())
print()
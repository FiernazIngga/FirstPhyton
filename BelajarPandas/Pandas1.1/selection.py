import pandas as pd
import os

os.system("cls")

# =====================================================
# LOAD DATA
# =====================================================

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, 'fileData', 'dataUntukLatihan.csv')

# index_col digunakan untuk menjadikan kolom tertentu
# sebagai index DataFrame (mengganti index 0,1,2,...)
df = pd.read_csv(file_path, index_col="Name")

# =====================================================
# SELEKSI DATA (COLUMNS & ROWS)
# =====================================================

# ---------------------
# Seleksi kolom
# ---------------------

# print(df["Height"].to_string())                     # Satu kolom
# print(df[["Height", "Weight"]].to_string())         # Beberapa kolom

# ---------------------
# Seleksi baris (ROWS)
# ---------------------

# Berdasarkan LABEL index (nama Pokemon)
# print(df.loc["Pikachu"])

# Berdasarkan LABEL + kolom tertentu
# print(df.loc["Charizard", ["Height", "Weight"]])

# Berdasarkan RENTANG LABEL (inklusif)
# print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])

# Berdasarkan POSISI index (0-based, akhir eksklusif)
# print(df.iloc[0:11])

# Baris loncat 2 + kolom 0 sampai 2
# print(df.iloc[0:11:2, 0:3])

# =====================================================
# INTERAKSI USER
# =====================================================

pokemon = input("Enter a Pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} tidak ditemukan")

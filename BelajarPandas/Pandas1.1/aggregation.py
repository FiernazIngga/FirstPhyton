import pandas as pd
import os

os.system("cls")

# =====================================================
# AGGREGATE FUNCTIONS (FUNGSI AGREGASI)
# -----------------------------------------------------
# Fungsi agregasi digunakan untuk MERANGKUM
# sekumpulan data menjadi satu nilai ringkasan.
#
# Contoh nilai ringkasan:
# - mean  : rata-rata
# - sum   : total
# - min   : nilai terkecil
# - max   : nilai terbesar
# - count : jumlah data
#
# Biasanya dipakai bersama groupby()
# untuk analisis per kategori.
# =====================================================

# Ambil path folder tempat file .py ini berada
base_dir = os.path.dirname(__file__)

# Gabungkan path folder dengan lokasi file CSV
file_path = os.path.join(base_dir, 'fileData', 'dataUntukLatihan.csv')

# Baca file CSV ke dalam DataFrame
df = pd.read_csv(file_path)

# =====================================================
# AGREGASI UNTUK SELURUH DATAFRAME
# (HANYA KOLOM NUMERIK)
# =====================================================

# print(df.mean(numeric_only=True))   # Rata-rata setiap kolom numerik
# print(df.sum(numeric_only=True))    # Total setiap kolom numerik
# print(df.min(numeric_only=True))    # Nilai minimum tiap kolom numerik
# print(df.max(numeric_only=True))    # Nilai maksimum tiap kolom numerik
# print(df.count())                   # Jumlah data (non-NaN) per kolom

# =====================================================
# AGREGASI UNTUK SATU KOLOM SAJA
# =====================================================

# print("Rata-rata Height :", df["Height"].mean())
# print("Total Height     :", df["Height"].sum())
# print("Height terendah  :", df["Height"].min())
# print("Height tertinggi:", df["Height"].max())
# print("Jumlah data      :", df["Height"].count())

# =====================================================
# GROUP BY (AGREGASI BERDASARKAN KATEGORI)
# =====================================================

# Mengelompokkan data berdasarkan kolom Type1
group = df.groupby("Type1")

# Contoh agregasi pada setiap grup Type1
# print(group["Height"].mean())   # Rata-rata Height per Type1
# print(group["Height"].sum())    # Total Height per Type1
# print(group["Height"].min())    # Height terendah per Type1
# print(group["Height"].max())    # Height tertinggi per Type1
# print(group["Height"].count())  # Jumlah data per Type1

import pandas as pd
import os

os.system("cls")

# =====================================================
# DATA CLEANING
# -----------------------------------------------------
# Data cleaning = proses memperbaiki atau menghapus
# data yang:
# - tidak lengkap (missing)
# - salah / inconsistent
# - tidak relevan
#
# Perlu dicatat: ~75% pekerjaan di pandas
# biasanya terkait data cleaning.
# =====================================================

# Ambil folder tempat file .py berada
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, 'fileData', 'dataUntukLatihan.csv')

# Baca CSV
df = pd.read_csv(file_path)

# =====================================================
# 1. DROP COLUMNS TIDAK RELEVAN
# =====================================================
# df = df.drop(columns=["No", "Legendary"])

# =====================================================
# 2. HANDLE MISSING DATA
# =====================================================
# Hapus baris yang Type2-nya kosong
# df = df.dropna(subset=["Type2"])

# Atau isi dengan nilai default
# df = df.fillna({"Type2": "Data aneh"})

# =====================================================
# 3. FIX INCONSISTENT VALUES
# =====================================================
# df["Type1"] = df["Type1"].replace({
#     "Grass": "GRASS",
#     "Fire": "FIRE",
#     "Water": "WATER"
# })

# =====================================================
# 4. STANDARDIZE TEXT
# =====================================================
# df["Name"] = df["Name"].str.lower()  # semua nama jadi huruf kecil

# =====================================================
# 5. FIX DATA TYPE
# =====================================================
# df["Legendary"] = df["Legendary"].astype(bool)

# =====================================================
# 6. REMOVE DUPLICATE VALUES
# =====================================================
df = df.drop_duplicates()  # hapus baris duplikat jika ada

# =====================================================
# MENAMPILKAN DATA
# =====================================================
print(df.to_string())

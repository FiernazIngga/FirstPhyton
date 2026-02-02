import os
os.system("cls")  # Bersihkan layar console supaya output rapi

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np

# ============================================================
# DATA CONTINUOUS & CATEGORICAL
# ============================================================
df = pd.DataFrame({
    'country': ['India','US','Japan','US','Japan'],  # kategori negara
    'age': [44,34,46,35,23],                         # umur, numerik
    'salary': [72000,65000,98000,45000,34000]       # gaji, numerik
})
print("=== Data asli ===")
print(df)
print()

# ============================================================
# 1️⃣ LABEL ENCODING
# ============================================================
# LabelEncoder → ubah kategori menjadi angka tunggal
# Cocok untuk label/target, tapi bisa salah kalau dipakai sebagai input
# Karena angka bisa dianggap ada urutan padahal kategori sebenarnya tidak
label_encoder = LabelEncoder()

df['country'] = label_encoder.fit_transform(df['country'])
# Misal:
# India → 0, Japan → 1, US → 2
# Angka ini HANYA sebagai ID, bukan ranking
print("=== Setelah Label Encoding ===")
print(df)
print()
# Analogi:
# Bayangkan nomor antrean di kasir:
# India=0, Japan=1, US=2
# Tidak ada yang lebih besar/kecil, tapi model bisa salah paham kalau dipakai input

# ============================================================
# 2️⃣ ONE-HOT ENCODING
# ============================================================
# Kita reset df untuk contoh one-hot
df = pd.DataFrame({
    'country': ['India','US','Japan','US','Japan'],
    'age': [44,34,46,35,23],
    'salary': [72000,65000,98000,45000,34000]
})
print("=== Data asli (untuk One-Hot) ===")
print(df)
print()

# Ambil kolom country sebagai fitur input
X = df['country'].values.reshape(-1,1)
# reshape(-1,1) → bentuk array harus 2D (baris,bukan kolom) supaya OneHotEncoder bisa dipakai
print("=== Country reshape(-1,1) ===")
print(X)
print()

# OneHotEncoder → ubah kategori jadi kolom biner (0/1)
onehot_encoder = OneHotEncoder()
X_onehot = onehot_encoder.fit_transform(X).toarray()
# Hasil:
# India → [1,0,0]
# Japan → [0,1,0]
# US    → [0,0,1]
print("=== Setelah One-Hot Encoding (array) ===")
print(X_onehot)
print()

# Buat DataFrame dari hasil one-hot encoding
df_onehot = pd.DataFrame(X_onehot, columns=[str(i) for i in range(X_onehot.shape[1])])
print("=== One-Hot DataFrame ===")
print(df_onehot)
print()

# Gabungkan hasil one-hot dengan data asli
df = pd.concat([df_onehot, df], axis=1)
print("=== Gabungan One-Hot & Original ===")
print(df)
print()

# Hapus kolom country asli, karena sudah ada one-hot
df = df.drop(['country'], axis=1)
print("=== Final DataFrame (One-Hot siap pakai) ===")
print(df)
print()

# ============================================================
# 🔑 Kesimpulan:
# ============================================================
# 1. LabelEncoder
#    - Output: angka tunggal per kategori
#    - Cocok untuk target (y)
#    - Risiko: kalau dipakai fitur input, model bisa salah paham urutan
#    - Analogi: nomor antrean kasir
#
# 2. OneHotEncoder
#    - Output: banyak kolom 0/1
#    - Cocok untuk fitur input
#    - Tidak ada urutan palsu
#    - Analogi: lampu indikator per kategori, setiap kategori setara

# =========================
# Program: Preprocessing Data (Versi Mudah Dipahami)
# =========================

import os
import numpy as np
from sklearn import preprocessing
os.system("cls")


# -------------------------
# 1. Data Contoh
# -------------------------
# Anggap data ini adalah data mentah dari dunia nyata
# Setiap baris = 1 objek (misalnya 1 orang)
# Setiap kolom = ciri-ciri objek tersebut
sample_data = np.array([
    [2.1, -1.9, 5.5],
    [-1.5,  2.4, 3.5],
    [0.5, -7.9, 5.6],
    [5.9,  2.3, -5.8]
])

print("=== Data Asli ===")
print(sample_data)
print()

# Analogi:
# Ini seperti data orang:
# tinggi, berat, dan umur
# Angkanya masih campur dan belum disesuaikan


# -------------------------
# 2. Binarization (Ya / Tidak)
# -------------------------
# Binarization mengubah angka menjadi:
# 1 = ya / aktif
# 0 = tidak / non-aktif

# Kita cuma peduli:
# "melewati batas atau tidak"
binarizer = preprocessing.Binarizer(threshold=0.5)
binarized_data = binarizer.transform(sample_data)

print("=== Binarization (0 dan 1) ===")
print(binarized_data)
print()

# Analogi:
# Seperti nilai ujian
# Nilai >= 75 → LULUS (1)
# Nilai < 75  → TIDAK LULUS (0)

# Kita tidak peduli nilainya 80 atau 95,
# yang penting lulus atau tidak


# -------------------------
# 3. Min-Max Scaling (Menyamakan Skala)
# -------------------------
# Di dunia nyata, angka bisa punya ukuran berbeda
# Contoh:
# umur: 20 - 60
# gaji: 3.000.000 - 30.000.000

# Komputer akan menganggap gaji jauh lebih penting
# hanya karena angkanya lebih besar

# MinMaxScaler menyamakan semuanya
# ke rentang yang mirip (0 sampai 1)
minmax_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
scaled_data = minmax_scaler.fit_transform(sample_data)

print("=== Min-Max Scaling ===")
print(scaled_data)
print()

# Analogi:
# Seperti lomba:
# ada yang diukur pakai meter
# ada yang diukur pakai kilometer

# Kalau mau dibandingkan adil,
# semua harus pakai satuan yang sama


# -------------------------
# 4. L1 Normalization (Melihat Perbandingan)
# -------------------------
# L1 Normalization membuat data dilihat sebagai perbandingan
# Bukan nilai aslinya

# Total tiap baris dianggap 100%
l1_normalized_data = preprocessing.normalize(sample_data, norm='l1')

print("=== L1 Normalization ===")
print(l1_normalized_data)
print()

# Analogi:
# Pengeluaran bulanan:
# makan  = 2 juta
# kos    = 1 juta
# hiburan = 1 juta

# Kita lebih paham kalau dilihat:
# makan 50%
# kos 25%
# hiburan 25%

# Bukan soal besar uang,
# tapi bagian mana yang paling besar


# -------------------------
# 5. L2 Normalization (Melihat Pola)
# -------------------------
# L2 Normalization membuat besar kecil angka
# jadi kurang penting

# Komputer fokus ke pola atau arah data
l2_normalized_data = preprocessing.normalize(sample_data, norm='l2')

print("=== L2 Normalization ===")
print(l2_normalized_data)
print()

# Analogi:
# Dua orang jalan ke arah yang sama:
# Orang A jalan 1 km
# Orang B jalan 10 km

# Arah mereka sama, cuma jaraknya beda

# L2 membantu komputer fokus ke arah,
# bukan seberapa jauh jalannya


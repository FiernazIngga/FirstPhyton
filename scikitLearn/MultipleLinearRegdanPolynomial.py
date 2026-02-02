import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

os.system("cls")

# ============================================================
# DATA TRAIN (DATA YANG DIPAKAI BELAJAR MODEL)
# ============================================================
pizza = {
    'diameter': [6, 8, 10, 14, 18],   # ukuran pizza (inch)
    'n_toping': [2, 1, 0, 2, 0],      # jumlah topping
    'harga': [7, 9, 13, 17.5, 18]     # harga pizza (target)
}

# Analogi:
# Ini seperti catatan toko pizza lama:
# "Kalau diameter segini dan topping segini, dulu dijual harga segini"

train_pizza_df = pd.DataFrame(pizza)

# ============================================================
# DATA TEST (DATA BARU UNTUK MENGECEK MODEL)
# ============================================================
pizza = {
    'diameter': [8, 9, 11, 16, 12],
    'n_toping': [2, 0, 2, 2, 0],
    'harga': [11, 8.5, 15, 18, 11]
}

# Analogi:
# Ini pelanggan baru, model BELUM PERNAH lihat data ini
# Kita pakai buat ngetes: model pinter beneran atau cuma hafalan

test_pizza_df = pd.DataFrame(pizza)

# ============================================================
# MULTIPLE LINEAR REGRESSION
# (pakai diameter + topping)
# ============================================================

# X_train = fitur (yang diketahui)
# y_train = target (yang mau ditebak)
X_train = np.array(train_pizza_df[['diameter', 'n_toping']])
y_train = np.array(train_pizza_df['harga'])

X_test = np.array(test_pizza_df[['diameter', 'n_toping']])
y_test = np.array(test_pizza_df['harga'])

# Model Linear Regression
# Rumus dasarnya:
# harga = a + b1*diameter + b2*topping
model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi harga pizza test
y_pred = model.predict(X_test)

# R² score → seberapa dekat prediksi ke data asli
print(f'r_squared (Multiple Linear): {r2_score(y_test, y_pred)}')

# Analogi:
# Model ini seperti:
# "Setiap tambah diameter sekian inch → harga naik sekian
#  Setiap tambah topping → harga naik sekian"
# Semua pengaruh dianggap LURUS (linear)

# ============================================================
# POLYNOMIAL REGRESSION
# Fokus ke diameter saja supaya gampang divisualisasikan
# ============================================================

# Ambil diameter saja
# reshape(-1,1) artinya:
# - kolomnya 1 (diameter saja)
# - barisnya bebas sesuai jumlah data
X_train = np.array(train_pizza_df['diameter']).reshape(-1, 1)
y_train = np.array(train_pizza_df['harga'])

# ============================================================
# VISUALISASI
# ============================================================

# Buat titik X dari 0 sampai 25 (buat gambar garis halus)
X_vis = np.linspace(0, 25, 100).reshape(-1, 1)

# ============================================================
# 1️⃣ LINEAR REGRESSION (GARIS LURUS)
# ============================================================

# Asumsi:
# "Setiap diameter naik 1 inch,
#  harga selalu naik jumlah yang sama"

model = LinearRegression()
model.fit(X_train, y_train)
y_vis = model.predict(X_vis)

plt.plot(X_vis, y_vis, '--r', label='Linear')

# Analogi:
# Seperti tarif parkir flat:
# mau parkir 1 jam atau 10 jam,
# kenaikannya selalu sama

# ============================================================
# 2️⃣ QUADRATIC REGRESSION (MELENGKUNG HALUS)
# ============================================================

# degree=2 → tambahin X²
# Jadi model bisa "melengkung"
quadratic_feature = PolynomialFeatures(degree=2)

# Ubah X jadi:
# [1, X, X²]
X_train_quadratic = quadratic_feature.fit_transform(X_train)

model = LinearRegression()
model.fit(X_train_quadratic, y_train)

X_vis_quadratic = quadratic_feature.transform(X_vis)
y_vis = model.predict(X_vis_quadratic)

plt.plot(X_vis, y_vis, '--g', label='Quadratic')

# Kenapa quadratic penting?
# Karena di dunia nyata:
# - Pizza kecil → naik harga pelan
# - Pizza sedang → naik cepat
# - Pizza besar → mahal banget
#
# Ini JARANG lurus sempurna

# ============================================================
# 3️⃣ CUBIC REGRESSION (LEBIH LENTUR, BISA BELOK)
# ============================================================

# degree=3 → tambahin X³
# Model jadi sangat fleksibel
cubic_feature = PolynomialFeatures(degree=3)

X_train_cubic = cubic_feature.fit_transform(X_train)

model = LinearRegression()
model.fit(X_train_cubic, y_train)

X_vis_cubic = cubic_feature.transform(X_vis)
y_vis = model.predict(X_vis_cubic)

plt.plot(X_vis, y_vis, '--y', label='Cubic')

# Catatan penting:
# Cubic itu PEDANG BERMATA DUA
# ✔ Bisa nangkap pola rumit
# ❌ Gampang overfitting
#
# Analogi:
# Anak yang hafal jawaban ujian,
# tapi ga ngerti konsep

# ============================================================
# TAMPILKAN GRAFIK
# ============================================================

plt.title('Perbandingan diameter dan harga pizza')
plt.xlabel('Diameter (inch)')
plt.ylabel('Harga (dollar)')
plt.xlim(0, 25)
plt.ylim(0, 25)
plt.grid(True)
plt.legend()
plt.show()

# ============================================================
# INTI FILOSOFI MODEL
# ============================================================

# Kita TIDAK otomatis pakai model paling kompleks
# Urutan berpikir yang benar:
#
# 1. Coba Linear → paling sederhana
# 2. Kalau kurang pas → Quadratic
# 3. Cubic → hanya kalau benar-benar perlu
#
# Prinsip ML:
# "Model sesederhana mungkin, tapi masih masuk akal"

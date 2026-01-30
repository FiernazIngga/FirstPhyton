# =========================
# Program: Prediksi Harga Pizza dengan Linear Regression
# =========================
# Tujuan: Menebak harga pizza berdasarkan diameter
# Menggunakan garis lurus terbaik dari data contoh
# =========================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Membersihkan layar terminal (hanya supaya tampilan rapi)
os.system("cls")


# -------------------------
# 1. Membuat Data Pizza
# -------------------------
# Setiap baris = 1 pizza
# Kolom 'diameter' = ukuran pizza
# Kolom 'harga' = harga pizza
pizza = {'diameter': [6,8,10,14,18],
         'harga': [7,9,13,17.5,18]}

pizza_df = pd.DataFrame(pizza)
print("=== Data Pizza ===")
print(pizza_df)
print()

# Analogi:
# Ini seperti tabel harga di menu pizza
# Kita mau tahu hubungan ukuran dan harga


# -------------------------
# 2. Visualisasi Data
# -------------------------
pizza_df.plot(kind='scatter', x='diameter', y='harga')
plt.title('Perbandingan Diameter dan Harga Pizza')
plt.xlabel('Diameter (inch)')
plt.ylabel('Harga (dollar)')
plt.xlim(0, 25)
plt.ylim(0, 25)
plt.grid(True)
# plt.show()  # aktifkan kalau mau lihat grafik

# Analogi:
# Titik-titik ini adalah pizza nyata di dunia
# Diameter vs harga, biar kita bisa lihat pola


# -------------------------
# 3. Menyiapkan Data untuk Model
# -------------------------
X = np.array(pizza_df['diameter'])  # fitur (diameter)
y = np.array(pizza_df['harga'])     # target (harga)

print(f'X (diameter): {X}')
print(f'y (harga): {y}')

# Ubah bentuk X supaya cocok untuk model
X = X.reshape(-1, 1)
print(f'Bentuk X setelah reshape: {X.shape}')
print(X)
print()

# Analogi:
# Komputer ingin data dalam bentuk tabel kolom (bukan daftar biasa)


# -------------------------
# 4. Training Linear Regression Model
# -------------------------
model = LinearRegression()
model.fit(X, y)

# Analogi:
# Komputer melihat data pizza dan menarik garis lurus terbaik
# untuk memperkirakan harga berdasarkan diameter


# -------------------------
# 5. Visualisasi Garis Prediksi
# -------------------------
X_vis = np.array([0, 25]).reshape(-1,1)  # dari diameter 0 sampai 25
y_vis = model.predict(X_vis)

plt.scatter(X, y)          # data asli
plt.plot(X_vis, y_vis, '-r')  # garis prediksi
plt.title('Perbandingan Diameter dan Harga Pizza')
plt.xlabel('Diameter (inch)')
plt.ylabel('Harga (dollar)')
plt.xlim(0, 25)
plt.ylim(0, 25)
plt.grid(True)
# plt.show()  # aktifkan kalau mau lihat grafik

print(f'intercept (harga dasar): {model.intercept_}')
print(f'slope (kenaikan harga tiap inch): {model.coef_}')
print()

# Analogi:
# Harga pizza = intercept + slope * diameter
# Misal: intercept = 2, slope = 0.9 → harga = 2 + 0.9*diameter


# -------------------------
# 6. Menghitung Slope Manual (opsional)
# -------------------------
# Slope = seberapa curam garisnya
# Rumus matematika: slope = covariance / variance

variance_x = np.var(X.flatten(), ddof=1)
coveriance_xy = np.cov(X.flatten(), y)[0][1]
slope_manual = coveriance_xy / variance_x

print(f'Variance X: {variance_x}')
print(f'Covariance X dan Y: {coveriance_xy}')
print(f'Slope manual: {slope_manual}')

# Intercept manual
intercept_manual = np.mean(y) - slope_manual * np.mean(X)
print(f'Intercept manual: {intercept_manual}')
print()

# Analogi:
# Kita bisa hitung sendiri kemiringan garis tanpa library
# Tapi biasanya cukup pakai LinearRegression saja


# -------------------------
# 7. Prediksi Harga Pizza Baru
# -------------------------
diameter_pizza = np.array([12, 20, 23]).reshape(-1,1)
prediksi_harga = model.predict(diameter_pizza)

for dmtr, hrg in zip(diameter_pizza, prediksi_harga):
    print(f'Diameter: {dmtr[0]} inch → Prediksi harga: ${hrg:.2f}')

print()
# Analogi:
# Misal ada pizza 12 inch, komputer bisa prediksi harganya


# -------------------------
# 8. Evaluasi Model (R-squared)
# -------------------------
# Split data menjadi training dan testing (contoh)
X_train = np.array([6,8,10,14,18]).reshape(-1,1)
y_train = np.array([7,9,13,17.5,18])

X_test = np.array([8,9,11,16,12]).reshape(-1,1)
y_test = np.array([11,8.5,15,18,11])

# Training model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi testing
y_pred = model.predict(X_test)

# Evaluasi
r_squared = r2_score(y_test, y_pred)
print(f'R-squared (seberapa cocok garis): {r_squared}')

# Analogi:
# R² = 1 → prediksi sempurna
# R² = 0 → prediksi nggak berguna
# Ini bilang seberapa dekat tebakan komputer ke harga asli

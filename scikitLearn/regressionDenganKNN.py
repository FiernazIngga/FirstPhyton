import os
os.system("cls")
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelBinarizer, StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# LabelBinarizer → ubah kategori (pria/wanita) jadi angka supaya bisa dihitung
# StandardScaler → scaling fitur agar semua fitur punya bobot seimbang
# KNeighborsRegressor → model KNN untuk prediksi angka (regresi)
# mean_absolute_error, mean_squared_error, r2_score → evaluasi akurasi model

# -------------------------
# 1. Data Contoh
# -------------------------
sensus = {
    'tinggi': [158, 170, 183, 191, 155, 163, 180, 158, 178],
    'berat':  [64,  86,  84,  80,  49,  59,  67,  54,  67],
    'jk': [
        'pria','pria','pria','pria',
        'wanita','wanita','wanita','wanita','wanita'
    ]
}
# Analogi: tabel KTP. Baris = satu orang, kolom = tinggi, berat, jenis kelamin

df = pd.DataFrame(sensus)
print("=== Data Sensus ===")
print(df)
print()

# -------------------------
# 2. Preprocess fitur
# -------------------------
X = df['tinggi']         # ambil kolom tinggi
lb = LabelBinarizer()                  
jk_num = lb.fit_transform(df['jk']).flatten()  # ubah jk: pria=0, wanita=1
# flatten → ubah array 2D ([[0],[1]]) jadi 1D ([0,1,...])
X = np.column_stack((X, jk_num))       # gabungkan tinggi + jk → array fitur
y = df['berat'].to_numpy()             # target = berat badan

print("=== X_train ===")
print(X)
print("=== y_train ===")
print(y)
print()
# Analogi: X_train = info yang diketahui (tinggi + jk)
# y_train = info yang ingin ditebak (berat)
# Seperti guru punya data tinggi & jk siswa dan ingin menebak berat mereka

# -------------------------
# 3. Scaling fitur
# -------------------------
scaler = StandardScaler()              # inisialisasi scaler
X_scaled = scaler.fit_transform(X)     # ubah X_train supaya rata-rata=0, std=1
print("=== X_train scaled ===")
print(X_scaled)
print()
# Analogi: bayangkan tinggi 180 cm dan jk=1
# Tanpa scaling → tinggi lebih besar daripada jk → KNN terlalu fokus ke tinggi
# Scaling → semua fitur seimbang → prediksi lebih adil

# -------------------------
# 4. Training KNN Regression
# -------------------------
model = KNeighborsRegressor(n_neighbors=3)  # n_neighbors=3 → lihat 3 tetangga terdekat
model.fit(X_scaled, y)                       # model “belajar” dari data
# Analogi: KNN seperti bertanya ke tetangga:
# "Orang mirip ini beratnya berapa?"
# Model ambil 3 tetangga terdekat → rata-rata → prediksi berat

# -------------------------
# 5. Prediksi data baru
# -------------------------
X_new = np.array([[155, 1]])              # data baru: tinggi=155, jk=wanita
X_new_scaled = scaler.transform(X_new)    # scaling sama seperti train
y_pred = model.predict(X_new_scaled)      # prediksi berat
print(f"Prediksi berat orang baru: {y_pred[0]:.2f} kg")
print()
# Analogi: model bertanya ke 3 tetangga terdekat orang baru
# Lalu rata-rata berat mereka → tebakan model

# -------------------------
# 6. Evaluasi test set
# -------------------------
X_test = np.array([[168,0],[180,0],[160,1],[169,1]])  # data baru untuk cek akurasi
y_test = np.array([65,96,52,67])                      # nilai asli
X_test_scaled = scaler.transform(X_test)             # scaling sama seperti train
y_pred_test = model.predict(X_test_scaled)          # prediksi

print("=== Prediksi Test Set ===")
for i, pred in enumerate(y_pred_test):
    print(f"Data {i+1}: Prediksi={pred:.2f}, Asli={y_test[i]}")
print()
# Analogi: seperti ujian → kita cek tebakan model vs data asli

# -------------------------
# 7. Metrics (menilai performa)
# -------------------------
r2 = r2_score(y_test, y_pred_test)                # R^2 → seberapa dekat prediksi vs asli (1 = perfect)
mae = mean_absolute_error(y_test, y_pred_test)    # MAE → rata-rata selisih absolut
mse = mean_squared_error(y_test, y_pred_test)     # MSE → rata-rata selisih kuadrat (lebih sensitif kesalahan besar)

print(f"R^2 score: {r2:.2f}")  
print(f"MAE: {mae:.2f}")  
print(f"MSE: {mse:.2f}")  
# Analogi:
# R^2 → model seberapa “percaya diri” prediksi (1 = sempurna, 0 = seperti tebak saja)
# MAE → rata-rata melenceng, misal ±2 kg
# MSE → sama dengan MAE tapi kesalahan besar dihukum lebih berat

# =========================
# Program: KNN Klasifikasi Jenis Kelamin
# (Versi Awam + Banyak Komentar)
# =========================

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelBinarizer
from sklearn.neighbors import KNeighborsClassifier

# Membersihkan layar terminal (khusus Windows)
os.system("cls")


# -------------------------
# 1. Data Sensus (Data Latih)
# -------------------------
# Anggap ini data nyata dari lapangan
# Setiap baris = 1 orang
# Kolom:
# - tinggi (cm)
# - berat (kg)
# - jk (jenis kelamin = label / kelas)

sensus = {
    'tinggi': [158, 170, 183, 191, 155, 163, 180, 158, 178],
    'berat':  [64,  86,  84,  80,  49,  59,  67,  54,  67],
    'jk': [
        'pria','pria','pria','pria',
        'wanita','wanita','wanita','wanita','wanita'
    ]
}

# Mengubah dictionary menjadi tabel (DataFrame)
sensus_df = pd.DataFrame(sensus)
print(sensus_df)
print()

# Analogi:
# Ini seperti tabel Excel berisi data orang-orang
# Model akan "menghafal" tabel ini


# -------------------------
# 2. Memisahkan Fitur dan Label
# -------------------------

# Fitur (X) = data yang dipakai untuk menebak
# HANYA angka → tinggi dan berat
XTrain = np.array(sensus_df[['tinggi', 'berat']])

# Label (y) = jawaban yang ingin ditebak
# Masih dalam bentuk teks: pria / wanita
yTrain = np.array(sensus_df['jk'])


# -------------------------
# 3. Encoding Label (Teks → Angka)
# -------------------------

# Komputer tidak paham teks
# Jadi pria / wanita harus diubah ke angka
lb = LabelBinarizer()

# Contoh hasil:
# pria   → 1
# wanita → 0
yTrain = lb.fit_transform(yTrain)

print(f'yTrain:\n{yTrain}\n')

# Karena hasilnya masih 2D ([[1],[0],...])
# Kita ratakan jadi 1D ([1,0,1,...])
yTrain = yTrain.flatten()

print(f'yTrain Flatten:\n{yTrain}')

# Analogi:
# Ini seperti:
# "YA / TIDAK" diubah jadi
# 1 / 0
# Supaya mesin bisa mikir


# -------------------------
# 4. Training Model KNN
# -------------------------

# Membuat model KNN
# n_neighbors=3 artinya:
# model akan melihat 3 orang paling mirip
model = KNeighborsClassifier(n_neighbors=3)

# "Training" di KNN sebenarnya cuma:
# menyimpan data ke memori
model.fit(XTrain, yTrain)

# Analogi:
# Ini seperti kamu menyimpan data semua orang
# Belum mengambil keputusan apa-apa


# -------------------------
# 5. Prediksi Data Baru
# -------------------------

# Orang baru (belum diketahui jenis kelaminnya)
tinggiBadan = 155
beratBadan  = 70

# Data baru HARUS berbentuk 2D array
XNew = np.array([tinggiBadan, beratBadan]).reshape(1, -1)

# Model mulai bekerja:
# 1. Hitung jarak ke semua data latih
# 2. Ambil 3 terdekat
# 3. Voting mayoritas
yNew = model.predict(XNew)

print(yNew)

# Mengubah hasil angka kembali ke teks
print(lb.inverse_transform(yNew))

# Analogi:
# Seperti nanya:
# "Dari 3 orang yang paling mirip,
# kebanyakan mereka pria atau wanita?"


# -------------------------
# 6. Visualisasi Data
# -------------------------

# Membuat kanvas gambar
fig, ax = plt.subplots()

# Menggambar titik berdasarkan jenis kelamin
for jk, d in sensus_df.groupby('jk'):
    ax.scatter(d['tinggi'], d['berat'], label=jk)

# Titik merah = orang misterius
plt.scatter(
    tinggiBadan,
    beratBadan,
    marker='s',
    color='red',
    label='misterius'
)

plt.legend(loc='upper left')
plt.title('Sebaran Data Tinggi, Berat, dan Jenis Kelamin')
plt.xlabel('Tinggi badan (cm)')
plt.ylabel('Berat badan (kg)')
plt.grid(True)

# plt.show()  # dinonaktifkan biar tidak auto muncul


# -------------------------
# 7. Menghitung Jarak Manual (Inti KNN)
# -------------------------

# Data orang misterius
misterius = np.array([tinggiBadan, beratBadan])

# Menggunakan jarak Euclidean (jarak lurus)
from scipy.spatial.distance import euclidean

# Hitung jarak ke setiap data latih
dataJarak = [euclidean(misterius, d) for d in XTrain]

print(dataJarak)

# Simpan jarak ke DataFrame
sensus_df['jarak'] = dataJarak

# Urutkan dari jarak terkecil
sensus_df.sort_values(['jarak'], inplace=True)

print(sensus_df)

# Analogi:
# Baris paling atas = orang paling mirip
# 3 baris teratas = tetangga KNN


# -------------------------
# 8. Data Testing (Evaluasi Model)
# -------------------------

# Data uji (tidak ikut dilatih)
xTest = np.array([
    [168,65],
    [180,96],
    [160,52],
    [169,67]
])

# Label asli (jawaban sebenarnya)
yTest = lb.transform(
    np.array(['pria','pria','wanita','wanita'])
).flatten()

print(f'xTest:\n{xTest}')
print(f'yTest:\n{yTest}\n')

# Prediksi model
yPred = model.predict(xTest)
print(yPred)


# -------------------------
# 9. Evaluasi Model
# -------------------------

# Accuracy = seberapa banyak yang benar
from sklearn.metrics import accuracy_score
acc = accuracy_score(yTest, yPred)
print(f'Accuracy: {acc}')

# Precision = kalau model bilang "pria",
# berapa yang benar-benar pria
from sklearn.metrics import precision_score
prec = precision_score(yTest, yPred)
print(f'Precision: {prec}')

# Recall = dari semua pria asli,
# berapa yang berhasil ketebak
from sklearn.metrics import recall_score
rec = recall_score(yTest, yPred)
print(f"Recall: {rec}")

# F1 = keseimbangan precision & recall
from sklearn.metrics import f1_score
f1 = f1_score(yTest, yPred)
print(f'F1-score: {f1}')

# Laporan lengkap
from sklearn.metrics import classification_report
cls_report = classification_report(yTest, yPred)
print(f'Classification Report:\n{cls_report}')

# MCC = metrik paling adil untuk data kecil
from sklearn.metrics import matthews_corrcoef
mcc = matthews_corrcoef(yTest, yPred)
print(f'MCC: {mcc}')

import os
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

os.system('cls')  # Bersihkan layar console supaya lebih rapi

# ===========================================================
# 1️⃣ Load Dataset
# ===========================================================
# load_breast_cancer → dataset bawaan scikit-learn tentang kanker payudara
# X = fitur (angka-angka seperti ukuran sel, tekstur, dll)
# y = label (0 = tidak kanker / benign, 1 = kanker / malignant)
X, y = load_breast_cancer(return_X_y=True)

# Analogi:
# Bayangkan X itu seperti tabel data pasien:
#   kolom = fitur (ukuran sel, kekasaran, dll)
#   baris = tiap pasien
# y = hasil dokter (benign atau malignant)

# ===========================================================
# 2️⃣ Bagi data jadi train dan test
# ===========================================================
# train_test_split → pisahkan data supaya model bisa belajar dan diuji
# test_size=0.2 → 20% data dijadikan test, 80% untuk training
# random_state=0 → supaya pembagian data sama setiap run (reproducible)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

print(f'X_train shape {X_train.shape}')  # Bentuk data training
print(f'X_test shape {X_test.shape}')    # Bentuk data testing
print()

# ===========================================================
# 3️⃣ Buat model Gaussian Naive Bayes
# ===========================================================
# GaussianNB → cocok untuk data numerik kontinu
# Asumsi: tiap fitur mengikuti distribusi Gaussian (bell curve)
model = GaussianNB()

# ===========================================================
# 4️⃣ Latih model
# ===========================================================
model.fit(X_train, y_train)
# Analogi:
# Model "belajar" dari data training:
#   melihat pola fitur → prediksi benign/malignant

# ===========================================================
# 5️⃣ Prediksi test set
# ===========================================================
y_pred = model.predict(X_test)
# Analogi:
# Model coba tebak label pasien baru (test set) berdasarkan yang dipelajari

# ===========================================================
# 6️⃣ Evaluasi akurasi
# ===========================================================
print(accuracy_score(y_test, y_pred))  # Rata-rata benar/total tebakan
print(model.score(X_test, y_test))     # Cara cepat scikit-learn → sama dengan accuracy

# Analogi:
# Accuracy = seberapa sering model menebak benar
# Misal 90% → dari 100 pasien, 90 tebakan benar

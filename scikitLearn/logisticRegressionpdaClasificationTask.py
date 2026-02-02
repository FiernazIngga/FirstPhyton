import os
import pandas as pd
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
os.system("cls")

# ====================================================
# 1️⃣ Load dataset SMS Spam Collection
# ====================================================
base_dir = os.path.dirname(__file__)  # Ambil folder skrip sekarang
file_path = os.path.join(base_dir, 'dataset/SMSSpamCollection')  # path file ZIP/CSV

# Baca dataset
# sep='\t' karena file dipisahkan tab
# header=None → file ga ada header
# names=[...] → beri nama kolom sendiri
df = pd.read_csv(file_path, sep='\t', header=None, names=['label','sms'])

# ====================================================
# 2️⃣ Pisahkan fitur dan target
# ====================================================
X = df['sms'].values  # Ambil kolom SMS sebagai fitur
y = df['label'].values  # Ambil kolom label ('ham' atau 'spam') sebagai target

# Analogi: X = teks SMS, y = apakah SMS itu spam/ham
# Contoh:
# X = "Free msg: claim your reward"
# y = "spam"

# Ubah label menjadi angka supaya bisa dipakai model
lb = LabelBinarizer()
y = lb.fit_transform(y).ravel()  # 'ham' → 0, 'spam' → 1
print("Classes:", lb.classes_)  # Lihat mapping label

# ====================================================
# 3️⃣ Split data menjadi train & test
# ====================================================
# 75% data untuk training, 25% untuk testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

# Analogi:
# Bayangkan guru punya 100 SMS:
# 75 SMS dipakai latihan (model belajar)
# 25 SMS disimpan untuk ujian (cek kemampuan model)

print("Contoh X_train:", X_train[:5])
print("Contoh y_train:", y_train[:5])
print()

# ====================================================
# 4️⃣ Feature extraction dengan TF-IDF
# ====================================================
# Teks harus diubah jadi angka agar model bisa mengolahnya
# TF-IDF = Term Frequency - Inverse Document Frequency
# → Memberi bobot kata berdasarkan pentingnya
# stop_words='english' → buang kata umum seperti 'the', 'is', 'a'
vectorizer = TfidfVectorizer(stop_words='english')

# Fit TF-IDF di data train → pelajari vocab dari X_train
X_train_tfidf = vectorizer.fit_transform(X_train)

# Transform X_test pakai vocab yang sama
X_test_tfidf = vectorizer.transform(X_test)

# Analogi:
# Anggap setiap kata di SMS punya nilai penting.
# Kata 'Free' sering muncul di spam → bobot tinggi
# Kata 'the' muncul di semua SMS → bobot rendah
print("Shape X_train_tfidf:", X_train_tfidf.shape)  # [jumlah_sms, jumlah_kata_unik]

# ====================================================
# 5️⃣ Binary classification dengan Logistic Regression
# ====================================================
model = LogisticRegression()  # Pilih model klasifikasi sederhana tapi kuat
model.fit(X_train_tfidf, y_train)  # Latih model

# Prediksi SMS test
y_pred = model.predict(X_test_tfidf)

# Tampilkan contoh prediksi
for pred, sms in zip(y_pred[:5], X_test[:5]):
    print(f'PRED: {pred} - SMS: {sms}\n')

# Analogi:
# Model = guru yang belajar mengenali spam
# Prediksi = guru menebak: spam atau ham berdasarkan kata-kata penting

# ====================================================
# 6️⃣ Penjelasan singkat
# ====================================================
# - X_train_tfidf: representasi numerik SMS (fitur)
# - y_train: label 0=ham, 1=spam
# - LogisticRegression: model mempelajari bobot kata untuk membedakan spam vs ham
# - TF-IDF: memastikan kata penting punya pengaruh besar, kata umum diabaikan
# - train_test_split: cek kemampuan model dengan data baru yang belum pernah dilihat

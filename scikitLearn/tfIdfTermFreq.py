import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

os.system("cls")
# =====================================================
# DATA TEKS (CORPUS)
# =====================================================
corpus = [
    'the house had a tiny little mouse',
    'the cat saw the mouse',
    'mouse ran away from the house',
    'the cat finally ate the mouse',
    'the end of the mouse story'
]

# corpus = kumpulan dokumen/kalimat
# Analogi:
# Seperti 5 paragraf cerita pendek tentang mouse & cat

# =====================================================
# TF-IDF VECTORIZER
# =====================================================
vectorizer = TfidfVectorizer(stop_words='english')
# TfidfVectorizer = pengembangan dari Bag of Words
#
# Perbedaannya:
# Bag of Words → hanya hitung jumlah kata
# TF-IDF       → hitung PENTING atau TIDAKNYA kata
#
# stop_words='english':
# Menghapus kata umum seperti:
# "the", "a", "from", dll
#
# Karena kata-kata ini:
# - sering muncul
# - tidak menjelaskan topik

response = vectorizer.fit_transform(corpus)
# fit_transform():
# 1. fit       → belajar semua kata unik
# 2. transform → hitung bobot TF-IDF tiap kata
#
# Output masih berupa sparse matrix
# (hemat memori, banyak nilai 0)

print(response)
print()

print(vectorizer.get_feature_names_out())
print()
# Menampilkan daftar kata (fitur)
# Ini adalah kolom dari vektor TF-IDF

print(response.toarray())
print()
# Mengubah sparse matrix menjadi array biasa
# Agar bisa dilihat nilainya secara nyata

# =====================================================
# APA ITU TF-IDF (PAKAI ANALOGI)
# =====================================================
# TF  (Term Frequency):
# → seberapa sering kata muncul dalam satu dokumen
#
# IDF (Inverse Document Frequency):
# → seberapa jarang kata muncul di semua dokumen
#
# Kata yang:
# - sering muncul di satu dokumen
# - tapi jarang muncul di dokumen lain
# → dianggap PALING PENTING

# Contoh analogi:
# Kata "mouse" muncul di semua dokumen
# → informatifnya kecil
#
# Kata "story" cuma muncul sekali
# → informatifnya besar

# =====================================================
# MEMBUAT DATAFRAME AGAR MUDAH DIPAHAMI
# =====================================================
df = pd.DataFrame(
    response.toarray().T,
    index=vectorizer.get_feature_names_out(),
    columns=[f'D{i+1}' for i in range(len(corpus))]
)

# response.toarray().T
# T (transpose) → dibalik:
# Baris  = kata
# Kolom = dokumen
#
# Analogi:
# Tabel nilai:
# Baris = nama siswa (kata)
# Kolom = mata pelajaran (dokumen)
# Isi   = skor kepentingan (TF-IDF)

print(df)

# =====================================================
# MANFAAT TF-IDF
# =====================================================
# 1. Kata umum tidak mendominasi analisis
# 2. Kata unik lebih dihargai
# 3. Lebih akurat untuk:
#    - pencarian dokumen
#    - clustering teks
#    - similarity teks
#    - machine learning NLP
#
# Singkatnya:
# TF-IDF = Bag of Words + logika + keadilan

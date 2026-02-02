import os
os.system("cls")  
from sklearn.feature_extraction.text import CountVectorizer
# CountVectorizer = alat untuk mengubah teks jadi angka
# Analogi: kamus penghitung kata
# Setiap kata = 1 kolom, setiap kalimat = 1 baris

from sklearn.metrics.pairwise import euclidean_distances
# euclidean_distances = menghitung jarak antar vektor
# Analogi: mengukur jarak dua titik di peta

# =====================================================
# DATA TEKS (CORPUS)
# =====================================================
corpus = [
    'Linux has been around sincer the mid-1990s.',
    'Linux distributtions include the Linux kernel.',
    'Linux is one of the most prominent open-source software'
]

# Analogi:
# corpus = kumpulan dokumen
# Seperti 3 artikel pendek tentang Linux

# =====================================================
# BAG OF WORDS (COUNT VECTORIZER)
# =====================================================
vectorizer = CountVectorizer()
# Membuat objek CountVectorizer
# Dia akan:
# 1. Memecah kalimat jadi kata
# 2. Membuat daftar semua kata unik
# 3. Menghitung berapa kali kata muncul di tiap dokumen

vectorized_X = vectorizer.fit_transform(corpus).toarray()
# fit_transform():
# - fit  → belajar kata apa saja yang ada
# - transform → ubah teks jadi angka
#
# toarray():
# - ubah dari format sparse matrix ke array biasa
#
# Hasil:
# Baris  = dokumen
# Kolom = kata
# Isi   = jumlah kemunculan kata

print(vectorized_X)
print(vectorizer.get_feature_names_out())
print()

# Analogi Bag of Words:
# Bayangkan tabel absensi:
# Dokumen | linux | kernel | software | ...
# Dok 1   |   1   |   0    |    0
# Dok 2   |   2   |   1    |    0
# Dok 3   |   1   |   0    |    1

# =====================================================
# EUCLIDEAN DISTANCE (JARAK ANTAR DOKUMEN)
# =====================================================
# Tujuan:
# Mengukur seberapa MIRIP dua dokumen
# Semakin kecil jarak → semakin mirip isinya

for i in range(len(vectorized_X)):
    for j in range(i, len(vectorized_X)):
        if i == j:
            continue
        # Kalau dokumen dibandingkan dengan dirinya sendiri
        # Jarak = 0 → tidak perlu dihitung

        jarak = euclidean_distances(
            vectorized_X[i].reshape(1, -1),
            vectorized_X[j].reshape(1, -1)
        )
        # reshape(1, -1):
        # Ubah vektor jadi 1 baris
        # Karena euclidean_distances butuh format 2D
        #
        # Analogi:
        # Kita mengukur jarak dua titik
        # Tapi titiknya punya banyak koordinat (kata)

        print(f'Jarak dokumen {i+1} dan {j+1}: {jarak}')

print()

# Analogi jarak dokumen:
# Dokumen = titik di peta
# Kata = arah mata angin
# Jarak kecil → topiknya mirip
# Jarak besar → topiknya beda

# =====================================================
# STOP WORD FILTERING
# =====================================================
vectorizer2 = CountVectorizer(stop_words='english')
# stop_words='english':
# Menghapus kata umum seperti:
# "is", "the", "one", "of", "has", dll
#
# Karena kata-kata ini:
# - sering muncul
# - tidak punya makna topik
#
# Analogi:
# Mengabaikan kata "dan", "yang", "di" saat menganalisis artikel

vectorized_X2 = vectorizer2.fit_transform(corpus).toarray()
# Proses sama seperti sebelumnya
# Tapi sekarang kata-kata tidak penting sudah dibuang

print(vectorized_X2)
print(vectorizer2.get_feature_names_out())
print()

# =====================================================
# KENAPA STOP WORD PENTING?
# =====================================================
# Tanpa stop word:
# Model bisa salah mengira dokumen mirip
# hanya karena sama-sama punya kata "is", "the", "one"
#
# Dengan stop word:
# Model fokus ke kata penting:
# "linux", "kernel", "software", dll
#
# Hasil:
# Perhitungan jarak lebih AKURAT

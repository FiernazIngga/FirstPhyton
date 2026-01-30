# =========================
# Program: Belajar Dataset Iris & Train/Test Split
# =========================

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

os.system("cls")  

# -------------------------
# 1 Load Dataset Iris
# -------------------------
iris = load_iris()  
# Dataset Iris berisi:
# - Fitur: panjang & lebar sepal, panjang & lebar petal
# - Target: jenis bunga (0=setosa, 1=versicolor, 2=virginica)

# -------------------------
# 2 Pisahkan Fitur dan Target
# -------------------------
# Fitur (Explanatory Variable)
X = iris.data
# X berisi angka panjang & lebar bunga
# Bentuknya: 150 baris (bunga), 4 kolom (fitur)

# Target (Response Variable)
y = iris.target
# y berisi kode kelas bunga: 0=setosa, 1=versicolor, 2=virginica
# Bentuknya: 150 baris, 1 kolom

# -------------------------
# 3 Nama Fitur & Target
# -------------------------
featureNames = iris.feature_names
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

targetNames = iris.target_names
# ['setosa', 'versicolor', 'virginica']

# -------------------------
# 4 Visualisasi Data (Scatter Plot)
# -------------------------
# Kita ambil dua fitur pertama: sepal length & sepal width
X_plot = X[:, :2]  
# X[:, :2] artinya:
# "ambil semua baris (:), tapi hanya kolom 0 dan 1 (:2)"

# Tentukan batas plot supaya titik nggak menempel di tepi
xmin, xmax = X_plot[:, 0].min() - 0.5, X_plot[:, 0].max() + 0.5
ymin, ymax = X_plot[:, 1].min() - 0.5, X_plot[:, 1].max() + 0.5

# Buat scatter plot
# Warna tiap titik berdasarkan kelas target
# plt.scatter(X_plot[:, 0], X_plot[:, 1], c=y)
# plt.xlabel('Sepal Length (cm)')
# plt.ylabel('Sepal Width (cm)')
# plt.xlim(xmin, xmax)
# plt.ylim(ymin, ymax)
# plt.grid(True)
# plt.show()

# -------------------------
# 5 Bagi Dataset Menjadi Training & Testing
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_plot,   # data fitur 2 kolom
    y,        # target
    test_size=0.3,     # 30% data untuk test, 70% untuk train
    random_state=1     # supaya hasil split selalu sama tiap run
)

# Bentuk data
print("=== Bentuk Dataset Setelah Split ===")
print(f"X_train: {X_train.shape} → 105 baris, 2 kolom")
print(f"X_test : {X_test.shape}  → 45 baris, 2 kolom")
print(f"y_train: {y_train.shape} → 105 baris (label)")
print(f"y_test : {y_test.shape}  → 45 baris (label)")

# -------------------------
# 6 Load Dataset sebagai Pandas DataFrame (opsional)
# -------------------------
iris_df = load_iris(as_frame=True)  # load langsung jadi DataFrame
iris_features_df = iris_df.data       # ambil kolom fitur saja
iris_target_df   = iris_df.target     # ambil kolom target saja

# Tampilkan DataFrame
print("\n=== Data Fitur (DataFrame) ===")
print(iris_features_df.head())  # tampil 5 baris pertama
print("\n=== Data Target (DataFrame) ===")
print(iris_target_df.head())    # tampil 5 baris pertama

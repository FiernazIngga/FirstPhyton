# -------------------------
# Import Library
# -------------------------
import os
import joblib          # untuk menyimpan & memuat model ML
from sklearn.datasets import load_iris          # dataset iris bawaan sklearn
from sklearn.model_selection import train_test_split  # untuk membagi data menjadi train & test
from sklearn.neighbors import KNeighborsClassifier   # model KNN
from sklearn.metrics import accuracy_score           # untuk menghitung akurasi
os.system("cls")


# -------------------------
# Load Dataset
# -------------------------
iris = load_iris()  # memuat dataset iris (150 baris, 4 fitur: sepal & petal)
X = iris.data       # X = semua fitur (angka panjang/lebar sepal & petal)
y = iris.target     # y = target / label bunga (0=setosa, 1=versicolor, 2=virginica)


# -------------------------
# Split Dataset menjadi Training & Testing
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.4,   # 40% data untuk testing, 60% data untuk training
    random_state=1   # supaya hasil split selalu sama setiap run
)

# Hasil split:
# X_train → data fitur untuk melatih model
# X_test  → data fitur untuk mengevaluasi model
# y_train → label target untuk melatih model
# y_test  → label target untuk mengevaluasi model


# -------------------------
# Training Model
# -------------------------
# KNeighborsClassifier → model KNN (K-Nearest Neighbors)
# n_neighbors=3 → model akan lihat 3 tetangga terdekat untuk memprediksi kelas
model = KNeighborsClassifier(n_neighbors=3)

# fit() → melatih model menggunakan data training
model.fit(X_train, y_train)


# -------------------------
# Evaluasi Model
# -------------------------
# predict() → model memprediksi kelas untuk data testing
y_pred = model.predict(X_test)

# accuracy_score → menghitung persentase prediksi yang benar
acc = accuracy_score(y_test, y_pred)
print(f'Accuracy: {acc}')  # contoh output: 0.9666 → 96.66% benar


# -------------------------
# Pemanfaatan Trained Model untuk Data Baru
# -------------------------
data_baru = [
    [5, 5, 3, 2],  # data baru 1
    [2, 4, 3, 5]   # data baru 2
]

# Model memprediksi label untuk data baru
preds = model.predict(data_baru)
print(preds)  # akan menampilkan angka 0/1/2 sesuai target

# Ubah angka target menjadi nama bunga
pred_species = [iris.target_names[p] for p in preds]
print(f'Hasil Prediksi: {pred_species}')  
# Contoh output: ['versicolor', 'virginica']


# -------------------------
# Simpan & Load Model dengan Joblib
# -------------------------
# joblib.dump → menyimpan model ke file agar bisa dipakai nanti tanpa melatih ulang
joblib.dump(model, 'scikitLearn/modelTraining/iris_classifier_knn.joblib')  
# parameter:
# 1. model → model ML yang sudah dilatih
# 2. nama file → tempat menyimpan model

# joblib.load → memuat model dari file untuk prediksi lagi
production_model = joblib.load('scikitLearn/modelTraining/iris_classifier_knn.joblib')
print(production_model)  
# Output → informasi model, misal KNeighborsClassifier(n_neighbors=3)

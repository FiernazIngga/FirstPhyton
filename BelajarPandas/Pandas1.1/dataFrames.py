import pandas as pd
import os

os.system("cls")

# =====================================================
# DATAFRAME
# -----------------------------------------------------
# DataFrame adalah struktur data berbentuk tabel
# (2 dimensi: baris & kolom), mirip spreadsheet Excel.
# Setiap kolom punya nama, setiap baris punya index.
# =====================================================

# Data awal dalam bentuk dictionary
data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

# Membuat DataFrame dengan index custom
df = pd.DataFrame(
    data,
    index=["Employee 1", "Employee 2", "Employee 3"]
)

# =====================================================
# AKSES DATA
# =====================================================

# Akses baris berdasarkan LABEL index
# print(df.loc["Employee 1"])

# Akses baris berdasarkan POSISI index (0-based)
# print(df.iloc[0])

# =====================================================
# MENAMBAH KOLOM
# =====================================================

# Menambahkan kolom baru "Job"
df["Job"] = ["Cook", "N/A", "Cashier"]

# =====================================================
# MENAMBAH BARIS (ROW)
# =====================================================

# Data baris baru harus dibungkus DataFrame
new_row = pd.DataFrame(
    [
        {"Name": "Sandy", "Age": 28, "Job": "Engineer"},
        {"Name": "Eugene", "Age": 60, "Job": "Manager"}
    ],
    index=["Employee 4", "Employee 5"]
)

# Menggabungkan DataFrame lama dengan baris baru
df = pd.concat([df, new_row])

# =====================================================
# MENAMPILKAN DATA
# =====================================================

print(df)

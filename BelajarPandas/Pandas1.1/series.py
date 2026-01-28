import pandas as pd
import os

os.system("cls")

# =====================================================
# SERIES
# -----------------------------------------------------
# Series adalah struktur data pandas 1 dimensi
# yang memiliki:
# - index (label)
# - value (nilai)
#
# Bisa dianggap seperti SATU kolom pada tabel.
# =====================================================

# Data dalam bentuk dictionary
# key   -> index
# value -> data
calories = {
    "Day 1": 1750,
    "Day 2": 2100,
    "Day 3": 1700
}

# Membuat Series dari dictionary
series = pd.Series(calories)

# Menampilkan seluruh isi Series
print(series)

import pandas as pd
import os

os.system("cls")

# =====================================================
# LOAD DATA
# =====================================================

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, 'fileData', 'dataUntukLatihan.csv')

df = pd.read_csv(file_path)

# =====================================================
# FILTERING DATA
# -----------------------------------------------------
# Filtering = memilih baris (rows) yang memenuhi
# kondisi tertentu.
#
# Hasil filtering SELALU berupa DataFrame baru.
# =====================================================

# Pokemon dengan tinggi >= 2
tall_pokemon = df[df["Height"] >= 2]

# Pokemon dengan berat > 100
heavy_pokemon = df[df["Weight"] > 100]

# Pokemon Legendary
legendary_pokemon = df[df["Legendary"] == True]

# Pokemon bertipe Water
# (Type1 ATAU Type2 adalah "Water")
water_pokemon = df[
    (df["Type1"] == "Water") | (df["Type2"] == "Water")
]

# Pokemon Fire + Flying
# (Type1 HARUS Fire DAN Type2 HARUS Flying)
ff_pokemon = df[
    (df["Type1"] == "Fire") & (df["Type2"] == "Flying")
]

# =====================================================
# OUTPUT
# =====================================================

print(ff_pokemon)

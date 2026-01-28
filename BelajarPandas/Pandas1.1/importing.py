import pandas as pd
import os

os.system("cls")

# =====================================================
# MENENTUKAN BASE DIRECTORY
# -----------------------------------------------------
# base_dir menunjuk ke folder tempat file .py berada
# supaya path file tidak error walau dijalankan
# dari direktori mana pun.
# =====================================================

base_dir = os.path.dirname(__file__)

# =====================================================
# MEMBACA FILE CSV
# =====================================================

csv_path = os.path.join(base_dir, 'fileData', 'dataUntukLatihan.csv')
df = pd.read_csv(csv_path)

# =====================================================
# MEMBACA FILE JSON
# =====================================================

json_path = os.path.join(base_dir, 'fileData', 'dataUntukLatihan.json')
df_json = pd.read_json(json_path)

# =====================================================
# MENAMPILKAN DATA
# =====================================================

# to_string() digunakan untuk menampilkan
# SELURUH isi DataFrame tanpa terpotong
print(df_json.to_string())

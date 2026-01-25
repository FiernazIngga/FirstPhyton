import pandas as pd
import numpy as np
import os
os.system("cls")

data = {'col1': ['1','2','3','teks'],
        'col2': ['1','2','3','4']}

df = pd.DataFrame(data)

# df_x = hanya col2 ke float, col1 tetap seperti semula
df_x = df.copy()
df_x['col2'] = df_x['col2'].astype(float)

# df_y = hanya col1 diubah numeric, col2 tetap seperti semula
df_y = df.copy()
df_y['col1'] = pd.to_numeric(df_y['col1'], errors='coerce') # Coerce berati kalau ada yang erro atau tidak bisa diubah akan diganti NaN

print("df_x (col2 float):\n", df_x)
print("\nTipe data df_x:\n", df_x.dtypes)

print("\ndf_y (col1 numeric / NaN jika gagal):\n", df_y)
print("\nTipe data df_y:\n", df_y.dtypes)

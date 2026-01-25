import pandas as pd
import numpy as np
import os
os.system('cls')

# base_dir = os.path.dirname(__file__)
# file_path = os.path.join(base_dir, 'kapal_titanic.csv')

# Membuat sebuah tabel
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')
df = pd.DataFrame(np.random.randint(1,10,size=(n_rows, n_cols)), columns=cols)

# Memberi nama pada kolom_A, kolom_B....
# df = df.add_prefix('kolom_') # Menambah bagian depan A,B,C,D,E
df = df.add_suffix('_field') # Menambah bagian belakang A,B,C,D,E
print(df)
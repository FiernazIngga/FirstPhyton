import os
import numpy as np
os.system("cls")

a = np.array([(1,-1),(1,1)])

print(a)
print()

# Inverse matriks
a_inv = np.linalg.inv(a)
print(a_inv)
print()

# Determinan
det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)
print(det_a)
print(det_a_inv)
print()
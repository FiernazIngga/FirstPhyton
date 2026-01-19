import os
import numpy as np

os.system("cls")

vector = np.array([1,2,3,4])

# print(f"Ini adalah list vector = {vector**2}")

matriv = np.array([(1,2),(3,4)])
# print(matriv)

zeros = np.zeros((2,2))
# print(zeros)

ones = np.ones((2,2))
# print(ones)

jumlah = matriv + matriv**2 + ones
print(jumlah)
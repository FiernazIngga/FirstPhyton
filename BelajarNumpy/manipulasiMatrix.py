import os
import numpy as np
os.system("cls")

a = np.array(([1,2,3],[4,5,6]))

print("Matrix a dengan ukuran:", a.shape)
print(a)
print()

# Transpose matrix
print("Transpose matrix dari a:")
print(a.transpose())
# print(np.transpose(a))
# print(a.T)
print()

# Flatten array, vector baris
print("Flatten matrix a:")
print(a.ravel())
# print(np.ravel(a))
print()

# Reshape matrix
print("Reshape matrix a:")
print(a.reshape(3,2))
print(a.reshape(6,1))
print()

# Resize matrix
print("Resize matrix a:")
print(a.resize(3,2))
print(a) # Perbedaan dengan reshape, kalau resize akan merubah si a, sedangkan si reshape tidak akan mengubah si a
import os
import numpy as np
os.system("cls")

a = np.array(([1,2,5],[3,4,6]))
b = np.ones([3,1])

print("Matrix a: ")
print(a)
print()

print("Matrix b: ")
print(b)
print()

# Perkalian matrix
c = np.dot(a,b)
d = a.dot(b)

print("Hasil perkalian: ")
print(c)
print()
print(d)
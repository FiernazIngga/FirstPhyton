import os
import numpy as np
os.system("cls")

a = np.array([(2,3),(1,2)])
y = np.array([23,14])
print(a)
print()
print(y)
print()

aInv = np.linalg.inv(a)

# Menyelesaikan persamaan linear
x = np.dot(aInv, y) # Perkalian dot antara matriks invers dari a dan matriks y
print(x)
print()

# Cara lain
x2 = np.linalg.solve(a,y)
print(x2)
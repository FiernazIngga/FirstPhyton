import os
import numpy as np
os.system("cls")

a = np.array([1,2,3])
b = np.array([4,5,6])

aMath = np.zeros((2,3))
bMath = np.ones((2,3))

# Stacking matrix, menumpuk matrix
c = np.hstack((a,b))
d = np.vstack((a,b))

cMath = np.hstack((aMath, bMath))
dMath = np.vstack((aMath, bMath)) # Perhatikan ukuran matrix, jangan beda atau error

print(c)
print()
print(d)
print()
print(cMath)
print()
print(dMath)
print()
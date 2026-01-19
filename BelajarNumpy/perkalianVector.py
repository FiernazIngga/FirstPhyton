import os
import numpy as np
os.system("cls")

a = np.array([1,3])
b = np.array([3,0])

# Perkalian dot
c = np.dot(a,b)

# Perkalian cross
aCross = np.array([1,2,0])
bCross = np.array([2,1,0])
cCros = np.cross(aCross,bCross)
print(cCros)
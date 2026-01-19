import numpy as np
import os
os.system("cls")

# Membuat vector
a = np.array([1,2,3,4,5])
b = np.array([1.5, 2.5, 5,6,7])

# Membuat vector dengan range
c = np.arange(1,10,2)

# Membuat linspace
d = np.linspace(1,10,4) # membagi 1 sampai 10 kedalam 4 bagian dengan jarak yang sama

# Array multidimensi
e = np.array([(1,2,3),(4,5,6)])

# Matrix kosong dengan nilai 0
# f = np.zeros(5) # Ini adalah vector
f = np.zeros((5,5)) # Ini adalah matrix

# Matrix dengan nilai 1
g = np.ones((5,5))

# Matrix identitas
h1 = np.identity(5)
h2 = np.eye(5)

# Display
print(h2)
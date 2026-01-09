import os
os.system('cls')

data_0 = [1,2]
data_1 = [3,4]
data2D = [data_0, data_1, 10]
data2DCopy = data2D.copy()
print(f"Data      = \n{data2D}\n")
print(f"Data copy = \n{data2DCopy}\n")

# Memangambil
data = data2D[0][0]
print(f"Data = \n{data}\n")

# Address semuanya
print(f"Address data2D     = {hex(id(data2D))}")
print(f"Address data2DCopy = {hex(id(data2DCopy))}\n")

print("Address dari member ke 1\n")

print(f"Address data2D     = {hex(id(data2D[0]))}")
print(f"Address data2DCopy = {hex(id(data2DCopy[0]))}")

data2D[0][0] = 5
data2D[2] = 9
print(f"Data      = \n{data2D}\n")
print(f"Data copy = \n{data2DCopy}\n")

# Menggunakan deep copy

from copy import deepcopy

data_2D = [data_0, data_1, 10]
data_2D_deepCopy = deepcopy(data_2D)

print(f"Address data2D         = {hex(id(data_2D))}")
print(f"Address data2DDeepCopy = {hex(id(data_2D_deepCopy))}\n")

print("Address dari member ke 1\n")

print(f"Address data2D         = {hex(id(data_2D[0]))}")
print(f"Address data2DDeepCopy = {hex(id(data_2D_deepCopy[0]))}\n")

data_2D_deepCopy[0][0] = 10
print(f"Data      = \n{data_2D}\n")
print(f"Data deep = \n{data_2D_deepCopy}\n")
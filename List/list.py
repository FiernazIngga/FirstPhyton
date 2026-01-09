import os
os.system('cls')

# Kumpulan data numbers
data_angka = [1,2,3,4,5]
print(data_angka)

# Kumpulan data string
data_string = ["Ucup", "Otong" , "Odah"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, False]
print(data_boolean)

# Kumpulan campuran
data_campuran = [1, "Bala-bala", 2, "Cireng", "Ucup", True, "Otong", False]
print(data_campuran)

# Cara alternatif membuat list
data_range = range(0, 10, 2) # 2 itu digunakan kayak bertambah e 2, jadi ntar hasile 0,2,4,6,8
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat list dengan for loop, namanya list comprehension
list_pake_for = [i**2 for i in range(0,10)] # membuat list pake loop for dan i**2, tiap i dikuadratin
print(list_pake_for)

# Membuat list pake for pake if 
list_for_if = [i**2 for i in range(0,10) if i%2 == 0] # didalam list hanya berisikan angka genap dan tiap angka genap di kuadratin
print(list_for_if)

import os
os.system("cls")

# Kegunaan dari @property itu adalah biar method yang def
# diperlakukan selayaknya variable dan bukan fungsi, lihat 
# di bawah saat menggunakan atau mengganti dengan setter dan 
# getter tidak dengan armor(10) tapi sniper.armor = 10, kayak
# variable kan 

class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "Nama {}: \n\tHealth: {}".format(self.__name, self.__health)
        
    @property # Membuat sebuah method sebagai variable
    def info(self): # Pakai ini ketika ingin update bagian name, health agar diperbarui juga, kalo ga pake ini ga bisa berubah
        return "Nama {}: \n\tHealth: {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("Armor di delete")
        self.__armor = None

sniper = Hero("Sniper", 100, 10)

print("Merubah info")
print(sniper.info)
sniper.name = "Dadang"
print(sniper.info)
print()

print("Getter dan setter untuk armor")
print(sniper.armor)
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)
print()

print("Delete armor")
del sniper.armor
print(sniper.__dict__)
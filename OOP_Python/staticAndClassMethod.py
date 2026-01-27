import os
os.system("cls")

class Hero:
    # Private class variable
    __jumlah = 0
    
    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # Method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah

    # Method ini tidak berlaku untuk objek karena tidak ada self nya
    def getJumlah1(): # Method berlaku untuk class karena ga pakai self
        return Hero.__jumlah

    # Method static (Decorator) / bisa untuk dua duanya ga kayak yang atas itu
    @staticmethod # Nempel ke objek dan class
    def getJumlah2(): 
        return Hero.__jumlah
    
    @classmethod # Biar Hero.__jumlah, Hero nya bisa fleksible, ga hardcode
    def getJumlah3(cls):
        return cls.__jumlah


sniper = Hero("Sniper")
print(Hero.getJumlah2())
print(sniper.getJumlah2())
rikimaru = Hero("Rikimaru")
print(Hero.getJumlah3())
print(rikimaru.getJumlah3())
drowranger = Hero("Drow Ranger")
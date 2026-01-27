import os
os.system("cls")

class Hero:
    # Class variable
    jumlah = 0
    __privateJumlah = 0
    def __init__(self, name, health):
        self.name = name
        self.health = health

        # Variable instance private
        self.__private = "private"

        # Variable instance protected
        self._protected = "protected"

lina = Hero("Lina", 100)
print(lina.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)
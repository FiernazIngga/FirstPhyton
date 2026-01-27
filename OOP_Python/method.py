import os
os.system("cls")

class Hero:
    # Class variable class yang menempel ke class
    jumlahHero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlahHero += 1

    # Method tanpa return
    def siapa(self): 
        print("Namaku adalah " + self.name)

    # Method dengan argumen
    def healthUp(self, up):  
        self.health += up

    # Method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero("Sniper", 100, 10, 5)
hero2 = Hero("Mario Bros", 90, 5, 10)

hero1.siapa()
hero1.healthUp(10)
print(hero1.getHealth())
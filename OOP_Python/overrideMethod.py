import os
os.system("cls")

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("Show info di class")
        print("{} Health {}".format(self.name, self.health))

class HeroIntel(Hero):
    def __init__(self, name, health = 100):
        super().__init__(name, health)
    
    def showInfo(self):
        print("Show info di class HeroIntelligent")
        print("{} \n\tTipe: Intelligent, \n\tHealth: {}".format(self.name, self.health))

class HeroStrenght(Hero):
    def __init__(self, name, health = 200):
        super().__init__(name, health)

lina = HeroIntel("Lina")
axe = HeroStrenght("Axe")

axe.showInfo()

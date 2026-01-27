import os
os.system("cls")

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health {}".format(self.name, self.health))

class HeroInteligent(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 100)
        super().__init__(name, 100)
        # Hero.showInfo(self)
        super().showInfo()

class HeroStrenght(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 200)
        super().__init__(name, 200)
        super().showInfo()

lina = HeroInteligent("Lina")
axe = HeroStrenght("Axe")
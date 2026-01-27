import os
os.system("cls")

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Hero_intelligent(Hero):
    pass

class Hero_Strenght(Hero):
    pass

lina = Hero("Lina", 100)
techies = Hero_intelligent("Techies", 50)
axe = Hero_Strenght("Axe", 200)

print(lina.__dict__)
print(techies.__dict__)
print(axe.__dict__)
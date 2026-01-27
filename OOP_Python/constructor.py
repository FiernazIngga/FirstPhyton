import os
os.system("cls")

class Hero: # Template
    def __init__(self, name, atkPwr, health, armorHealth): # Self itu adalah hero1 atau objeknya itu sendiri
        self.name = name
        self.health = health
        self.attackPower = atkPwr
        self.armor = armorHealth

hero1 = Hero("Sniper", 200, 10, 4)
hero2 = Hero("Mirana", 30, 100, 10)

print(hero1.__dict__)
print(hero2.__dict__)
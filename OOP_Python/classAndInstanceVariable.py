import os
os.system("cls")

class Hero: # Template
    # Class variable
    jumlah = 0

    def __init__(self, name, atkPwr, health, armorHealth): # Self itu adalah hero1 atau objeknya itu sendiri
        # Instance variable
        self.name = name
        self.health = health
        self.attackPower = atkPwr
        self.armor = armorHealth
        Hero.jumlah += 1
        print("Membuat hero dengan name ", self.name)

hero1 = Hero("Sniper", 200, 10, 4)
print(Hero.jumlah)
hero2 = Hero("Mirana", 30, 100, 10)
print(Hero.jumlah)
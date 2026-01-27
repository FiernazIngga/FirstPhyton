import os
os.system("cls")

class Hero:
    def __init__(self, name, health, power):
        self.__name = name
        self.__health =  health
        self.__power = power

    # Getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health

    # Setter
    def diserang(self, atkPower):
        self.__health -= atkPower

    def setAttPower(self, nilaiBaru):
        self.__power = nilaiBaru

# Awal dari game
eShaker = Hero("Earth Shaker", 50, 5)

# print(eShaker.__name) # Ga bisa akses private variable
print(eShaker.getName())
print(eShaker.getHealth())
eShaker.diserang(5)
print(eShaker.getHealth())

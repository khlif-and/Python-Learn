from ctypes import ArgumentError
class hero:
    def __init__(self, name, type, damage, health, cooldownTime):
        self.name = name
        self.type = type
        self.damage = damage
        self.health = health
        self.cooldownTime = cooldownTime

    def info(self):
        print(f"ini adalah {self.name}, type {self.type}, damage {self.damage}, health {self.health}, cooldownTime {self.cooldownTime}")
    
    def check_type(self):
        if self.type == "Tank":
            print("Tank adalah hero yang memiliki health tinggi dan damage rendah")
        elif self.type == "Fighter":
            print("Fighter adalah hero yang memiliki health tinggi dan damage tinggi")
        elif self.type == "Marksman":
            print("Marksman adalah hero yang memiliki health rendah dan damage tinggi")
        elif self.type == "Mage":
            print("Mage adalah hero yang memiliki health rendah dan damage tinggi")
        elif self.type == "Support":
            print("Support adalah hero yang memiliki health tinggi dan damage rendah")
        elif self.type == "Assassin":
            print("Assassin adalah hero yang memiliki health rendah dan damage tinggi")
        else:
            print("Type hero tidak ditemukan")
        

class Tank(hero):
    def __init__(self, name, type, damage, health, cooldownTime, armor):
        super().__init__(name, type, damage, health, cooldownTime)
        
        self.armor = armor
    
    def info(self):
        super().info()
        print(f"armor {self.armor}")

gatotkaca = Tank("Gatotkaca", "Tank", 100, 1000, 10, 100)
gatotkaca.info()
gatotkaca.check_type()

    
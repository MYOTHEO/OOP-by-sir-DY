class Animal():
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def describeHero(self):
            print(f"Brand: {self.name} has {self.health}")
    
class Fish(Fish):
    def __init__(self, name, health, can_swim):
        super().__init__(name, health)
        self.can_swim = can_swim

miya = Fish("Miya","200","Malayuang Barilan")
print(miya.can_swim)
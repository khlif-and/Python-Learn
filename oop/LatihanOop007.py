class Animals:
    def __init__(self, name, kingdom, age, type):
        self.name = name
        self._kingdom = kingdom
        self.age = age
        self.type = type

    def info(self):
        print(f"ini adalah {self.name}, kingdom {self._kingdom}, umur {self.age}, type {self.type}")


class Cat(Animals):
    def __init__(self, name, kingdom, age, type, color, tailLength):
        super().__init__(name, kingdom, age, type)
        self.color = color
        self.tailLength = tailLength
    
    def info(self):
        super().info()
        print(f"color {self.color}, tailLength {self.tailLength}")

class Dog(Animals):
    def __init__(self, name, kingdom, age, type):
        super().__init__(name, kingdom, age, type)


list_animal = [Cat("Milo", "Animal", 2, "Cat", "Black", 10), Dog("Dog", "Animal", 2, "Dog")]

for animal in list_animal:
    animal.info()


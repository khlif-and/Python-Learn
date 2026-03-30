class Transport:
    def __init__(self, name, type, brand, price):
        self.name = name
        self.type = type
        self.brand = brand
        self.price = price

    def info(self):
        print(f"ini adalah {self.name}, type {self.type}, brand {self.brand}, harga {self.price}")


class Car(Transport):
    def __init__(self, name, type, brand, price, wheels, color):
        super().__init__(name, type, brand, price)
        self.wheels = wheels
        self.color = color

    def info(self):
        super().info()
        print(f"wheels {self.wheels}, color {self.color}")
    

class Motorcycle(Transport):
    def __init__(self, name, type, brand, price):
        super().__init__(name, type, brand, price)


list_type = [Car("Car", "Car", "Brand", 100000, 4, "Red"), Motorcycle("Motorcycle", "Motorcycle", "Brand", 100000)]

for trans in list_type:
    trans.info()
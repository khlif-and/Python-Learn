class Transport:
    def __init__(self, name, type, brand, price):
        self.set_name(name)
        self.type = type
        self.brand = brand
        self.price = price

    def info(self):
        print(f"ini adalah {self.__name}, type {self.type}, brand {self.brand}, harga {self.price}")

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name != "":
            self.__name = new_name
        else:
            raise ValueError("nama tidak boleh kosong")


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


list_type = [Car("Avanza", "Car", "Toyota", 100000, 4, "Red"), Motorcycle("Motorcycle", "Motorcycle", "Brand", 100000)]

for trans in list_type:
    trans.info()
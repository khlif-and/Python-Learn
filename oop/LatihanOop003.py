class Laptop:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def info(self):
        print(f"ini adalah {self.name}, brand {self.brand}, harga {self.price}")

class LaptopGaming(Laptop):
    def __init__(self, name, brand, price, vga):
        super().__init__(name, brand, price)
        self.vga = vga

    def info(self):
        super().info()
        print(f"vga {self.vga}")

AsusRog = LaptopGaming("Asus Rog", "Asus", 10000000, "RTX 3060")
AsusRog.info()
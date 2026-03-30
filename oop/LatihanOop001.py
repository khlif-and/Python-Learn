class Animal:
    def __init__(self, name, age, ras, location):
        self.name = name
        self.age = age
        self.ras = ras
        self.location = location
    
    def info(self):
        print(f"ini adalah {self.name}, berumur {self.age} tahun, ras {self.ras} dan tinggal di {self.location}")

kucing_saya = Animal("Milo", 2, "Persia", "Jakarta")
kucing_saya.info()
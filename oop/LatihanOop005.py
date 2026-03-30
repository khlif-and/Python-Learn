class Kendaraan:
    def __init__(self, name, plat, bahanBakar, namaKendaraan):
        self.name = name
        self.plat = plat
        self.__bahanBakar = bahanBakar
        self.namaKendaraan = namaKendaraan

    def info(self):
        print(f"ini adalah {self.name}, dengan plat {self.plat}, bahan bakar {self.__bahanBakar}, dan nama kendaraan {self.namaKendaraan}")


class Mobil(Kendaraan):
    def __init__(self, name, plat, bahanBakar, namaKendaraan, jumlahPintu, jenisMobil):
        super().__init__(name, plat, bahanBakar, namaKendaraan)
        self.jumlahPintu = jumlahPintu
        self.jenisMobil = jenisMobil

    def info(self):
        super().info()
        print(f"jumlah pintu {self.jumlahPintu}, jenis mobil {self.jenisMobil}")

namaMobil = Mobil("Mobil", "Plat", "Bahan Bakar", "Nama Mobil", 4, "Sedan")
namaMobil.info()
class Kucing:
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur

    def mengeong(self):
        print(f"{self.nama} sedang mengeong")

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Warna: {self.warna}")
        print(f"Umur: {self.umur}")

kucing1 = Kucing("Mochi", "Putih", 2)
kucing2 = Kucing("Oyen", "Orange", 3)

kucing1.mengeong()
kucing2.info()
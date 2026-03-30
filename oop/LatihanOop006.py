class Game:
    def __init__(self, name, genre, years, price):
        self.__name = name
        self.genre = genre
        self.years = years
        self.__price = price

    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("harga tidak boleh negatif")

    def info(self):
        print(f"ini adalah {self.__name}, genre {self.genre}, tahun {self.years}, harga {self.__price}")

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name != "":
            self.__name = new_name
        else:
            print("nama tidak boleh kosong")

my_game = Game("Game", "Genre", 2022, 100000)
my_game.info()
my_game.set_price(200000)
my_game.set_name("Game 2")
my_game.info()

    
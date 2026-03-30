class BankAccount:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.__balance = balance

    def info(self):
        print(f"ini adalah {self.name}, dengan id {self.id}, dan saldo {self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"deposit {amount} berhasil")
        else:
            print("deposit gagal")
    

account1 = BankAccount("1", "Khalif", 1000000)
account1.info()
account1.deposit(100000)

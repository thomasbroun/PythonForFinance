class Book:
    def __init__(self, name):
        self.name = name

    def insert_buy(self, amount, price):
        print("buy")

    def insert_sell(self, amount, price):
        print("sell")

class Order:
    def __init__(self, name):
        self.name = name

import itertools

class Book:

    def __init__(self, name):
        self.name = name
        self.orders = []

    def insert_buy(self, amount, price):
        neworder = Order("BUY", amount, price)  # Create a new order

        print("--- Insert BUY", amount, "@", price,
              "id=", neworder.idd, "on", self.name)  # print transaction

        self.orders.sort(key=lambda x: x.price, reverse=True)

        orderstodelete = []

        for order in self.orders:
            if (neworder.price >= order.price):
                if (order.ordertype == "SELL"):
                    amountleftinbook = order.amount - neworder.amount
                    # tout a ete execute / le book avait plus de stock que le nouvel ordre
                    if (amountleftinbook > 0):
                        print("Execute", neworder.amount, "at",
                              order.price, "on", self.name)
                        order.amount = amountleftinbook
                        neworder.amount = 0
                        break
                    if (amountleftinbook == 0):
                        print("Execute", neworder.amount, "at",
                              order.price, "on", self.name)
                        self.orders.remove(order)
                        neworder.amount = 0
                        break

                    else:  # not enough amount in book
                        print("Execute", order.amount, "at",
                              order.price, "on", self.name)
                        neworder.amount = neworder.amount - order.amount
                        order.amount = 0
                        orderstodelete.append(order)

        for order in orderstodelete:
            self.orders.remove(order)

        if neworder.amount > 0:
            self.addorder(neworder)
            self.orders.sort(key=lambda x: x.price, reverse=True)

        print("Book on", self.name)

        for order in self.orders:  # print the book
            print("\t", order.ordertype, order.amount,
                  "@", order.price, "id=", order.idd)

        print("----------------")

    def insert_sell(self, amount, price):
        neworder = Order("SELL", amount, price)  # Create a new order

        print("--- Insert SELL", amount, "@", price,
              "id=", neworder.idd, "on", self.name)  # print transaction

        self.orders.sort(key=lambda x: x.price, reverse=True)

        orderstodelete = []

        for order in self.orders:
            if (order.price >= neworder.price):
                if (order.ordertype == "BUY"):
                    amountleftinbook = order.amount - neworder.amount
                    # tout a ete execute / le book avait plus de stock que le nouvel ordre
                    if (amountleftinbook > 0):
                        print("Execute", neworder.amount, "at",
                              order.price, "on", self.name)
                        order.amount = amountleftinbook
                        neworder.amount = 0
                        break
                    if (amountleftinbook == 0):
                        print("Execute", neworder.amount, "at",
                              order.price, "on", self.name)
                        self.orders.remove(order)
                        break

                    else:  # not enough amount in book
                        print("Execute", order.amount, "at",
                              order.price, "on", self.name)
                        neworder.amount = neworder.amount - order.amount
                        order.amount = 0
                        orderstodelete.append(order)

        for order in orderstodelete:
            self.orders.remove(order)

        if neworder.amount > 0:
            self.addorder(neworder)
            self.orders.sort(key=lambda x: x.price, reverse=True)

        print("Book on", self.name)

        for order in self.orders:
            print("\t", order.ordertype, order.amount,
                  "@", order.price, "id=", order.idd)

        print("----------------")

    def addorder(self, order):
        self.orders.append(order)


class Order:
    id_iter = itertools.count()

    def __init__(self, ordertype, amount, price):
        self.idd = next(Order.id_iter) + 1
        self.amount = amount
        self.price = price
        self.ordertype = ordertype

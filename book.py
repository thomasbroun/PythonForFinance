import itertools
import pandas as pd

class Book:

    def __init__(self, name):
        self.name = name
        self.orders = []

    def insert_buy(self, amount, price):
        neworder = Order("BUY", amount, price)  # Create a new order

        print("--- Insert BUY", amount, "@", price,
              "id=", neworder.idd, "on", self.name)  # print transaction

        detailsorder = "--- Insert BUY ", str(amount), " @ ", str(price), " id=", str(neworder.idd), " on ", self.name


        self.orders.sort(key=lambda x: x.price, reverse=True)

        orderstodelete = []
        executestring = [] 

        for order in self.orders:
            if (neworder.price >= order.price):
                if (order.ordertype == "SELL"):
                    amountleftinbook = order.amount - neworder.amount
                    # tout a ete execute / le book avait plus de stock que le nouvel ordre
                    if (amountleftinbook > 0):
                        print("Execute", neworder.amount, "at",
                              order.price, "on", self.name)
                        executestr = "Execute " + str(neworder.amount) + " at " + str(order.price) + " on " + self.name
                        newstring = ''.join(executestr)
                        executestring.append(newstring)

                        order.amount = amountleftinbook
                        neworder.amount = 0
                        break
                    if (amountleftinbook == 0):
                        print("Execute", neworder.amount, "at",
                              order.price, "on", self.name)
                        executestr = "Execute " + str(neworder.amount) + " at " + str(order.price) + " on " + self.name
                        newstring = ''.join(executestr)
                        executestring.append(newstring)
                        self.orders.remove(order)
                        neworder.amount = 0
                        break

                    else:  # not enough amount in book
                        print("Execute", order.amount, "at",
                              order.price, "on", self.name)
                        executestr = "Execute " + str(order.amount) + " at " + str(order.price) + " on " + self.name
                        newstring = ''.join(executestr)
                        executestring.append(newstring)
                        neworder.amount = neworder.amount - order.amount
                        order.amount = 0
                        orderstodelete.append(order)

        for order in orderstodelete:
            self.orders.remove(order)

        if neworder.amount > 0:
            self.addorder(neworder)
            self.orders.sort(key=lambda x: x.price, reverse=True)

        print("Book on", self.name)

        buyordertypes = []
        buyorderamounts = []
        buyorderprices = []
        buyorderidds = []

        sellordertypes = []
        sellorderamounts = []
        sellorderprices = []
        sellorderidds = []

        for order in self.orders:
            print("\t", order.ordertype, order.amount,
                  "@", order.price, "id=", order.idd)
            if order.ordertype == "BUY":
                buyordertypes.append(order.ordertype)
                buyorderamounts.append(order.amount)
                buyorderprices.append(order.price)
                buyorderidds.append(order.idd)
            if order.ordertype == "SELL":
                sellordertypes.append(order.ordertype)
                sellorderamounts.append(order.amount)
                sellorderprices.append(order.price)
                sellorderidds.append(order.idd)

        buyside = {'Type': buyordertypes, 'Amount': buyorderamounts, 'Price': buyorderprices, 'Id': buyorderidds}
        sellside = {'Type': sellordertypes, 'Amount': sellorderamounts, 'Price': sellorderprices, 'Id': sellorderidds}

        dfbuy = pd.DataFrame(data=buyside)
        dfsell = pd.DataFrame(data=sellside)
        print()
        if dfbuy.empty:
            print()
            print("Empty buy book")
        else:
            print("-------- print buy side --------")
            print(dfbuy)
        
        if dfsell.empty:
            print("Empty sell book")
        else:
            print("-------- print sell side --------")
            print(dfsell)
        print()



    def insert_sell(self, amount, price):
        neworder = Order("SELL", amount, price)  # Create a new order

        detailsorder = "--- Insert SELL ", str(amount), " @ ", str(price), " id=", str(neworder.idd), " on ", self.name

        print("--- Insert SELL", amount, "@", price,
              "id=", neworder.idd, "on", self.name)  # print transaction

        self.orders.sort(key=lambda x: x.price, reverse=True)

        orderstodelete = []
        executestring = [] 

        for order in self.orders:
            if (order.price >= neworder.price):
                if (order.ordertype == "BUY"):
                    amountleftinbook = order.amount - neworder.amount
                    # tout a ete execute / le book avait plus de stock que le nouvel ordre
                    if (amountleftinbook > 0):
                        executestr = "Execute " + str(neworder.amount) + " at " + str(order.price) + " on " + self.name
                        newstring = ''.join(executestr)
                        executestring.append(newstring)
                        print("Execute", neworder.amount, "at",
                              order.price, "on", self.name)
                        order.amount = amountleftinbook
                        neworder.amount = 0
                        break
                    if (amountleftinbook == 0):
                        executestr = "Execute " + str(neworder.amount) + " at " + str(order.price) + " on " + self.name
                        newstring = ''.join(executestr)
                        executestring.append(newstring)
                        print("Execute", neworder.amount, "at",
                              order.price, "on", self.name)
                        self.orders.remove(order)
                        break

                    else:  # not enough amount in book

                        executestr = "Execute " + str(order.amount) + " at " + str(order.price) + " on " + self.name
                        newstring = ''.join(executestr)
                        executestring.append(newstring)
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

        buyordertypes = []
        buyorderamounts = []
        buyorderprices = []
        buyorderidds = []

        sellordertypes = []
        sellorderamounts = []
        sellorderprices = []
        sellorderidds = []

        for order in self.orders:
            print("\t", order.ordertype, order.amount,
                  "@", order.price, "id=", order.idd)
            if order.ordertype == "BUY":
                buyordertypes.append(order.ordertype)
                buyorderamounts.append(order.amount)
                buyorderprices.append(order.price)
                buyorderidds.append(order.idd)
            if order.ordertype == "SELL":
                sellordertypes.append(order.ordertype)
                sellorderamounts.append(order.amount)
                sellorderprices.append(order.price)
                sellorderidds.append(order.idd)

        buyside = {'Type': buyordertypes, 'Amount': buyorderamounts, 'Price': buyorderprices, 'Id': buyorderidds}
        sellside = {'Type': sellordertypes, 'Amount': sellorderamounts, 'Price': sellorderprices, 'Id': sellorderidds}

        dfbuy = pd.DataFrame(data=buyside)
        dfsell = pd.DataFrame(data=sellside)
        print()
        if dfbuy.empty:
            print()
            print("Empty buy book")
        else:
            print("-------- print buy side --------")
            print(dfbuy)
        
        if dfsell.empty:
            print("Empty sell book")
        else:
            print("-------- print sell side --------")
            print(dfsell)
        print()

    def addorder(self, order):
        self.orders.append(order)

    def currentbook(self):
        return self.orders
        


class Order:

    id_iter = itertools.count()

    def __init__(self, ordertype, amount, price):
        self.idd = next(Order.id_iter) + 1
        self.amount = amount
        self.price = price
        self.ordertype = ordertype

from book import Book
import pandas as pd
import numpy as np


def main():
    book = Book("TEST")
    # printtransactions(book.insert_buy(10, 10.0), book)
    # printtransactions(book.insert_sell(120, 12.0), book)
    # printtransactions(book.insert_buy(5, 10.0), book)
    # printtransactions(book.insert_buy(2, 11.0), book)
    # printtransactions(book.insert_sell(1, 10.0), book)
    # printtransactions(book.insert_sell(10, 10.0), book)

    book.insert_buy(10, 10.0)
    book.insert_sell(120, 12.0)
    book.insert_buy(5, 10.0)
    book.insert_buy(2, 11.0)
    book.insert_sell(1, 10.0)
    book.insert_sell(10, 10.0)


# def printtransactions(transaction, book):
#     print(''.join(transaction[0]))
#     print('Book on ', book.name)
#     if transaction[1]:
#         for items in transaction[1]:
#             print(items)
#     for order in book.orders:
#     	print("\t", order.ordertype, order.amount, "@", order.price, "id=", order.idd)
#     print("----------------")


if __name__ == "__main__":
    main()


# data = np.array([['','Col1','Col2'],
#                 ['Row1',1,2],
#                 ['Row2',3,4]])

# a = np.empty(shape=(25, 2), dtype=int)
# for x in range(1, 6):
#     for y in range(1, 6):
#         index = (x-1)*5+(y-1)
#         a[index] = x, y

# print(pd.DataFrame(data=a[1:,1:],
#                   index=a[1:,1],
#                   columns=a[1,1:]))

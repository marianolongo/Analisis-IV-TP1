import math
from decimal import Decimal


def a():
    return math.exp(1)


def b(n):
    sum = 0
    for i in range(n):
        sum = sum + 1.0 / (math.factorial(i))
    return sum


def c(n):
    sum = 0
    for i in range(n):
        sum = sum + Decimal(1.0 / (math.factorial(i)))
    return sum


def d(n):
    print('2.', end='')
    my_list = list()

    for i in range(n):
        my_list.insert(i, 1)

    for i in range(n):
        q = 0
        j = n - 1
        while j >= 0:
            my_list[j] = 10 * my_list[j] + q
            q = my_list[j] // (j + 2)
            my_list[j] = my_list[j] % (j + 2)
            j = j - 1
        print(q, end='')


if __name__ == '__main__':
    # print(NumberE.getEFromLibrary(NumberE))
    # print(NumberE.getEFloat(NumberE, 15))
    # print(NumberE.getEDecimal(NumberE, 15))
    d(100)

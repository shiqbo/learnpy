def add1(n):
    return n + 1

l = [3, 2, 5, 9, 7, 8, 6]

print(list(map(add1, l)))

print(list(map(lambda x: x + 1, l)))


def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, l)))

print(list(filter(lambda x: x % 2 == 0, l)))


from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, l))

print(reduce(lambda x, y: x + y, l))
print(reduce(lambda x, y: x + y, l, initial=10))

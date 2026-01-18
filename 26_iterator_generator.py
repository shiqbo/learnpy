from collections.abc import Iterable

"""
print(isinstance('hello world', Iterable))
print(isinstance([124, 456], Iterable))
print(isinstance({124, 456}, Iterable))
print(isinstance((124, 456), Iterable))
print(isinstance(124, Iterable))
print(isinstance({'a': 124, 'b': 345}, Iterable))


l = [100, 110, 120, 130]

i = iter(l)
print(i)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
"""

# iterator

class MyIterator:
    def __init__(self):
        self.current = 100

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 140:
            raise StopIteration
        result = self.current
        self.current = self.current + 10
        return result

i = MyIterator()
for j in i:
    print(j)
#print(next(i))


# generator 1

print([i * 3 for i in range(10)])
print((i * 3 for i in range(10)))

g = (i * 3 for i in range(10))
print(next(g))
print(next(g))

for i in g:
    print(i)


# generator 2

def gen():
    print('start')
    yield 100
    yield 200
    yield 300
    yield 400
    print('end')

g = gen()
print(g, type(g))

for i in g:
    print(i)
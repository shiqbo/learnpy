def task1():
    while True:
        yield 123
        yield 'abc'


def task2():
    while True:
        yield 456
        yield 'def'


if __name__ == '__main__':
    t1 = task1()
    t2 = task2()

    print(next(t1))
    print(next(t2))

    print(next(t1))
    print(next(t2))
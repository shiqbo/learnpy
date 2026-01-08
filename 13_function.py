def say_hi():
    print('hi')

'''
say_hi()
say_hi()
say_hi()
'''


def greet(name):
    print(f'hi {name}')

# greet('john')


def coffee(water, sugar, coffee=1):
    print(water, sugar, coffee)

coffee(1, 2)
coffee(1, 2, 2)


def summ(*args):
    s = 0
    for i in args:
        s += i
    print(s)

summ()
summ(1)
summ(1, 2, 3, 4)


def create_account(username, password, **kwargs):
    print(username)
    print(password)
    for i in kwargs.items():
        print(i)


create_account('john', 'abc123', age=18, gender='male', city='peking')


# return value
def meow():
    print('meow')
    return None

meow()


def add_num(i, j):
    return i + j

print(add_num(3, 4))


def talk():
    print('hello')
    return 'a', 'b', 'c'

r = talk()
print(r, type(r))

l, m, n = talk()
print(l, m, n, sep=';')

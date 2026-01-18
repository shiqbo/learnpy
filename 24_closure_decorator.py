# closure

'''
def outer():
    sugar = 'free'
    def inner():
        print(sugar)
    return inner

outer()()

def outer(i):
    def inner(j):
        print(f'{i} x {j} = {i*j}')
    return inner

outer(3)(4)
'''


# decorator

'''
def login_decorator(f):
    def wrapper():
        print('login successfully')
        f()
    return wrapper


def msg():
    print('message')


@login_decorator
def transfer():
    print('transfer')

login_decorator(msg)()

transfer()
'''

def login(f):
    def wrapper(*args, **kwargs):
        print('login')
        f(*args, **kwargs)
    return wrapper


@login
def msg(name):
    print(f'Send message to {name}')

msg('John')

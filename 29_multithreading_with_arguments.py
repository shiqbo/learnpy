import time
from threading import Thread

def sing(name):
    print(f'{name} is singing')
    time.sleep(3)
    print('done')

def dance(name):
    print(f'{name} is dancing')
    time.sleep(3)
    print('done')


if __name__ == '__main__':
    t1 = Thread(target=sing, args=('John',))
    t2 = Thread(target=dance, kwargs={'name': 'John'})
    t1.start()
    t2.start()
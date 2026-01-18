from multiprocessing import Process
import os


def sing(name):
    print(f'{name} is singing')
    print(os.getpid(), os.getppid())


def dance(name):
    print(f'{name} is dancing')
    print(os.getpid(), os.getppid())


if __name__ == '__main__':
    p1 = Process(target=sing, args=('John',), name='p1')
    p2 = Process(target=dance, kwargs={'name': 'John'}, name='p2')

    p1.start()

    p1.join()

    p2.start()

    print(p1.is_alive(), p2.is_alive())

    print(p1.name)
    print(p2.name)

    print(p1.pid)
    print(p2.pid)

    print(os.getpid(), os.getppid())
import time
from threading import Thread

def sing():
    print('sing')
    time.sleep(3)
    print('done')


def dance():
    print('dance')
    time.sleep(3)
    print('done')


if __name__ == '__main__':
    t1 = Thread(target=sing)
    t2 = Thread(target=dance)
    t1.start()
    t2.start()
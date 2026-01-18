from threading import Thread, Lock

a = 0
lock = Lock()


def add1():
    lock.acquire()
    for i in range(100000):
        global a
        a += 1
    print(a)
    lock.release()


def add2():
    lock.acquire()
    for i in range(100000):
        global a
        a += 1
    print(a)
    lock.release()


if __name__ == '__main__':
    # block main thread
    '''G
    t1 = Thread(target=add1)
    t1.start()
    t1.join()
    t2 = Thread(target=add2)
    t2.start()
    '''

    # gil
    t3 = Thread(target=add1)
    t3.start()
    t4 = Thread(target=add2)
    t4.start()
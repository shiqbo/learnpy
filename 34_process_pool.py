from multiprocessing import Pool
import time


def task(n):
    print('~')
    time.sleep(2)
    return n * 3


if __name__ == '__main__':
    p = Pool(3)

    l = []

    for i in range(7):
        r = p.apply_async(task, args=(i,))
        print(r)
        l.append(r)

    p.close()
    p.join()

    for i in l:
        print(i.get())
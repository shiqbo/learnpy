import multiprocessing
from multiprocessing import Process, Queue

l = ['abc', 'def', 'ghi', 'jkl']


def task_write(q):
    for i in l:
        print(f'put {i} in queue')
        q.put(i)


def task_read(q):
    while True:
        if q.empty():
            break
        else:
            print('get from queue', q.get())


if __name__ == '__main__':
    multiprocessing.set_start_method('fork', force=True)
    q = Queue()
    p1 = Process(target=task_write, args=(q,))
    p2 = Process(target=task_read, args=(q,))

    p1.start()
    p1.join()
    p2.start()
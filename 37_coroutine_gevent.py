import time
import gevent
from gevent import monkey

monkey.patch_all()

def sing():
    print('sing')
    time.sleep(1)
    print('sing done')


def dance():
    print('dance')
    gevent.sleep(2)
    print('dance done')


if __name__ == '__main__':
    # t1 = gevent.spawn(sing)
    # t2 = gevent.spawn(dance)

    # t1.join()
    # t2.join()

    gevent.joinall([
        gevent.spawn(sing),
        gevent.spawn(dance),
    ])
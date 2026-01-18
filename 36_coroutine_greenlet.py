from greenlet import greenlet


def sing():
    print('sing')
    g2.switch()
    print('sing done')


def dance():
    print('dance')
    print('dance done')
    g1.switch()


if __name__ == '__main__':
    g1 = greenlet(sing)
    g2 = greenlet(dance)

    g1.switch()
    # g2.switch()
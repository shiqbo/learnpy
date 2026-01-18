# Duck type

class WePay:
    def pay(self):
        print('wechat')


class AliPay:
    def pay(self):
        print('alibaba')


class UnionPay:
    def pay(self):
        print('bank')


def pay(obj):
    obj.pay()

pay(WePay())
pay(AliPay())
pay(UnionPay())


# inheritance + method overriding
class Animal:
    def speak(self):
        print('ing ing ing')


class Dog(Animal):
    def speak(self):
        print('wang wang wang')


class Cat(Animal):
    def speak(self):
        print('miao miao miao')


class Monkey(Animal):
    def speak(self):
        print('zhi zhi zhi')


def speak(obj):
    obj.speak()

speak(Animal())
speak(Dog())
speak(Cat())
speak(Monkey())

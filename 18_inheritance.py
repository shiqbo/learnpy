"""
class Life:
    feature = 'living'

    def breathe(self):
        print('breathe')


class Animal(Life):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('eating...')

    def sleep(self):
        print('sleeping...')

    def noise(self):
        print('ing ing ing...')


class Dog(Animal):
    def bark(self):
        print('woof')


class Cat(Animal):
    def noise(self):
        print('meow meow')


class Monkey(Animal):
    def noise(self):
        super().noise()
        print('zi zi zi')

dog = Dog('dog', 10)
print(dog.name, dog.age)
dog.eat()
dog.sleep()
dog.bark()
dog.breathe()

cat = Cat('cat', 10)
cat.noise()

monkey = Monkey('monkey', 10)
monkey.noise()
"""

class Watch:
    def show_time(self):
        print('cuttent time on watch')


class HealthDevice:
    def show_time(self):
        print('current time on health device')

    def check_heart_rate(self):
        print('heart rate')


class SmartWatch(Watch, HealthDevice):
    pass

sw = SmartWatch()
sw.show_time()
sw.check_heart_rate()
HealthDevice.show_time(sw)

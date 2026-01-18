# __new__ and __init__
"""
class House:
    def __new__(cls, *args, **kwargs):
        print('__new__')
        obj = object.__new__(cls)
        print(obj)
        return obj

    def __init__(self, addr, area):
        print('__init__')
        self.addr = addr
        self.area = area

h = House('Peking', 130)


class House:
    def __new__(cls, *args, **kwargs):
        print('__new__')
        obj = object.__new__(cls)
        print(obj)
        # without object reference


    def __init__(self, addr, area):
        print('__init__')
        self.addr = addr
        self.area = area

h = House('Peking', 130)


# singleton pattern
# rewrite __new__
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name

s1 = Singleton('John')
print(s1, id(s1))
s2 = Singleton('Anna')
print(s2, id(s2))

print(s1.name)
print(s2.name)


# singleton_module
from singleton_module unique_obj as obj1
from singleton_module unique_obj as obj2

print(id(obj1), id(obj2))
"""


# magic method

class Stu:
    """ Student class"""
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.gender}, {self.age}'

    def __del__(self):
        print('__del__')

    def __call__(self, *args, **kwargs):
        print('__call__')

stu = Stu('John', 'male', 18)
print(stu.__doc__)
print(stu.__class__)
print(stu.__module__)
print(stu.__dict__)
print(stu)
print(callable(stu))
stu()
del stu
print('hello')
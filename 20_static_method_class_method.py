# instance method
class Person:
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        print(f'hi, i am {self.name}')

per = Person('john')
per.sayhi()


# static method
class GeometryTool:
    @staticmethod
    def circle_area(radius):
        return 3.14 * radius ** 2

print(GeometryTool.circle_area(2))

a = GeometryTool()
print(a.circle_area(2))


# class method
class Person:
    average_age = 60

    @classmethod
    def get_average_age(cls):
        return cls.average_age

b = Person()
print(b.get_average_age())
b.average_age = 80  # !!
print(b.get_average_age())

print(Person.get_average_age())
Person.average_age = 70
print(Person.get_average_age())

class Car:
    wheel_count = 4

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def start(self):
        print(f'current object is {self}, {self.color} {self.brand} strating')

    def __del__(self):
        print(f'{self} destroyed')


car = Car('blue', '992')
print(car.wheel_count)
car.start()

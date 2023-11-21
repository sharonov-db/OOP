class Car:
    car_count = 0

    def __new__(cls):
        cls.car_count += 1
        return super().__new__(cls)

    def __del__(self):
        Car.__class__.car_count -= 1

    def __init__(self, name="Maclaren", make="Mercedes", year="2016"):
        self.name = name
        self.make = make
        self.year = year
        Car.__class__.car_count += 1

    def start(self):
        print('Engine started')

    def stop(self):
        print('Engine turned off')

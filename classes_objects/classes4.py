class Car:
    __car_count = 0

    @staticmethod
    def car_details():
        print('This is Car class')

    @classmethod
    def __inc_car_count(cls):
        cls.__car_count += 1

    @classmethod
    def __dec_car_count(cls):
        cls.__car_count -= 1

    @classmethod
    def get_car_count(cls):
        return cls.__car_count

    def __new__(cls):
        cls.inc_car_count()
        return super().__new__(cls)

    def __del__(self):
        self.dec_car_count()

    def __init__(self, name="Maclaren", make="Mercedes", year="2016"):
        self.name = name
        self.make = make
        self.year = year
        Car.__class__.car_count += 1

    def start(self):
        print('Engine started')

    def stop(self):
        print('Engine turned off')

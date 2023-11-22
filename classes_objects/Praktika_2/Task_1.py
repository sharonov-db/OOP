from math import pi


class Dot:

    def __init__(self, x, y, color='Black'):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"Координаты точки ({self.x}, {self.y}); Цвет - {self.color}"

    def __repr__(self):
        return self.__str__()


class Circle(Dot):
    def __int__(self, x, y, r=1):
        super().__init__(self, x, y)
        self.r = r

    def __str__(self):
        return f"Координаты центра ({self.x}, {self.y}); Цвет круга - {self.color}"

    def __repr__(self):
        return self.__str__()

    def get_area(self):
        return pi * self.r ** 2

    def set_radius(self, r):
        self.r = r


class Sphere(Circle):

    def __init__(self, x, y, r):
        super().__init__(self, x, y, r)

    def get_volume(self):
        return 4/3 * pi * self.r**3

    def get_area(self):
        return 4 * pi * self.r**2


class Car:

    def __init__(self, marka, model, sredrashod, sred_stoim_perevozki=0, capacity=100):
        self.sredrashod = sredrashod
        self.marka = marka
        self.model = model
        self.sred_stoim_perevozki = sred_stoim_perevozki
        self.capacity = capacity

    def get_rashod(self, km):
        return km * self.sredrashod

    def get_stoim(self, km):
        return km * self.sred_stoim_perevozki

    def __str__(self):
        return f"{self.marka} {self.model} Средний расход = {self.sredrashod} Мощность = {self.capacity}"

    def __repr__(self):
        return self.__str__()


class TaxiCar(Car):
    def __int__(self, marka, model, sredrashod, sred_stoim_perevozki=100, capacity=100):
        super().__init__(self, marka, model, sredrashod, sred_stoim_perevozki, capacity)

    free = False

    def __str__(self):
        return (f"Такси {self.marka} {self.model} Средний расход = {self.sredrashod} Мощность = {self.capacity}"
                f" Средняя стоимость проезда = {self.sred_stoim_perevozki}")

    def __repr__(self):
        return self.__str__()

    def set_free_car(self):
        self.free = True

    def set_none_free_car(self):
        self.free = False

    def get_is_car_free(self):
        return self.free


class GruzCar(TaxiCar):
    def __int__(self, marka, model, sredrashod, sred_stoim_perevozki=200, capacity=300):
        super().__init__(self, marka, model, sredrashod, sred_stoim_perevozki, capacity)

    dalnost_active_reisa = 1000

    def __str__(self):
        return (f"Грузовое Такси {self.marka} {self.model} Средний расход = {self.sredrashod} "
                f"Мощность = {self.capacity} Средняя стоимость проезда = {self.sred_stoim_perevozki}")

    def __repr__(self):
        return self.__str__()

    def set_dalnost_active_reisa(self, dalnost_active_reisa):
        self.dalnost_active_reisa = dalnost_active_reisa

    def get_dalnost_active_reisa(self):
        return self.dalnost_active_reisa

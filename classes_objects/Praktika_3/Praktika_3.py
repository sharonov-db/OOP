from math import pi
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def __init__(self, x, y, color='Black'):
        self.__x = x
        self.__y = y
        self.__color = color

    @abstractmethod
    def get_area(self):
        return 0

    def __repr__(self):
        return self.__str__()

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value


class Dot(Figure):

    def __init__(self, x, y, color='Black'):
        super().__init__(self, x, y, color)

    def __str__(self):
        return f"Координаты точки ({self.x}, {self.y}); Цвет - {self.color}"


class Circle(Dot):

    def __int__(self, x, y, r=1):
        super().__init__(self, x, y)
        self.__r = r

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, value):
        self.__r = value

    def set_radius(self, r):
        self.r = r

    def __str__(self):
        return f"Координаты центра ({self.x}, {self.y}); Цвет круга - {self.color}"

    def get_area(self):
        return pi * self.r ** 2


class Sphere(Circle):

    def __init__(self, x, y, r):
        super().__init__(self, x, y, r)

    def get_volume(self):
        return 4/3 * pi * self.r**3

    def get_area(self):
        return 4 * pi * self.r ** 2


class Auto(ABC):
    @abstractmethod
    def __init__(self, marka, model, sredrashod, sred_stoim_perevozki=0, capacity=100):
        self.__sredrashod = sredrashod
        self.__marka = marka
        self.__model = model
        self.__sred_stoim_perevozki = sred_stoim_perevozki
        self.__capacity = capacity


    def get_rashod(self, km):
        return km * self.sredrashod

    def get_stoim(self, km):
        return km * self.sred_stoim_perevozki

    def __repr__(self):
        return self.__str__()

    @property
    def marka(self):
        return self.__marka

    @marka.setter
    def marka(self, value):
        self.__marka = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def sredrashod(self):
        return self.__sredrashod

    @sredrashod.setter
    def sredrashod(self, value):
        self.__sredrashod = value

    @property
    def sred_stoim_perevozki(self):
        return self.__sred_stoim_perevozki

    @sred_stoim_perevozki.setter
    def sred_stoim_perevozki(self, value):
        self.__sred_stoim_perevozki = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value


class Car(Auto):
    def __init__(self, marka, model, sredrashod, sred_stoim_perevozki=0, capacity=100):
        super().__init__(self, marka, model, sredrashod, sred_stoim_perevozki, capacity)

    def __str__(self):
        return f"{self.marka} {self.model} Средний расход = {self.sredrashod} Мощность = {self.capacity}"


class TaxiCar(Car):
    def __int__(self, marka, model, sredrashod, sred_stoim_perevozki=100, capacity=100):
        super().__init__(self, marka, model, sredrashod, sred_stoim_perevozki, capacity)
        self.__free = False

    def __str__(self):
        return (f"Такси {self.marka} {self.model} Средний расход = {self.sredrashod} Мощность = {self.capacity}"
                f" Средняя стоимость проезда = {self.sred_stoim_perevozki}")

    @property
    def free(self):
        return self.__free

    @free.setter
    def free(self, value):
        self.__free = value

    def set_free_car(self):
        self.free = True

    def set_none_free_car(self):
        self.free = False

    def get_is_car_free(self):
        return self.free


class GruzCar(TaxiCar):
    def __int__(self, marka, model, sredrashod, sred_stoim_perevozki=200, capacity=300):
        super().__init__(self, marka, model, sredrashod, sred_stoim_perevozki, capacity)
        self.__dalnost_active_reisa = 1000

    @property
    def dalnost_active_reisa(self):
        return self.__dalnost_active_reisa

    @dalnost_active_reisa.setter
    def dalnost_active_reisa(self, value):
        self.__dalnost_active_reisa = value

    def __str__(self):
        return (f"Грузовое Такси {self.marka} {self.model} Средний расход = {self.sredrashod} "
                f"Мощность = {self.capacity} Средняя стоимость проезда = {self.sred_stoim_perevozki}")

    def set_dalnost_active_reisa(self, dalnost_active_reisa):
        self.dalnost_active_reisa = dalnost_active_reisa

    def get_dalnost_active_reisa(self):
        return self.dalnost_active_reisa


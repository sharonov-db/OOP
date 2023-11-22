import random


class List:

    list_1 = []

    def __init__(self, count):
        self.count = count

    def input_data(self, *args):
        list_2 = list()
        if len(args) != self.count:
            raise ValueError(f"Введите число элементов списка, равное {self.count}")
        else:
            for k in args:
                if isinstance(k, int):
                    list_2.append(k)
                else:
                    raise ValueError("Можно вводить только целочисленные элементы")

            self.list_1 = list_2

    def feel_random_data(self):
        list_2 = list()
        for k in range(self.count):
            list_2.append(random.randint(1, 1000))

        self.list_1 = list_2

    def __str__(self):
        return f"Список: {self.list_1}"

    def __repr__(self):
        return f"Список: {self.list_1}"

    def find_element(self, find_elem):
        list_index_finded = list()
        for item in self.list_1:
            if item == find_elem:
                list_index_finded.append(item)

        return list_index_finded

    def remove_element(self, elem):
        self.list_1.remove(elem)

    def __add__(self, other):
        list_sum = List(self.count)
        if self.count == other.count:
            if isinstance(self, List) and isinstance(other, List):
                for i in range(self.count):
                    list_sum.list_1.append(self.list_1[i] + other.list_1[i])
            else:
                raise TypeError("Списки принадлежат разным классам")
        else:
            raise ValueError("Списки имеют разное количество элементов")

        return list_sum.list_1


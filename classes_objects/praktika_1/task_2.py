import random


class List:

    list_1 = []

    def __init__(self, count):
        self.count = count

    def input_data(self, *args):
        list_2 = list()
        if args.count() != self.count:
            raise(f"Введите число элементов списка, равное {self.count}")
        else:
            for k in args:
                if isinstance(k, int):
                    list_2.append(k)

            self.list_1 = list_2

        return

    def feel_random_data(self):
        list_2 = list()
        for k in range(self.count):
            list_2.append(random.randint(1, 1000))

        self.list_1 = list_2

        return

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

        return

    def __add__(self, other):
        list_sum = list()
        if self.count() == other.count():
            for i in range(self.list_1.count()):
                if isinstance(self.list_1[i], int) and isinstance(other.list_1[i], int):
                    list_sum.append(self.list_1[i]+other.list_1[i])

        return



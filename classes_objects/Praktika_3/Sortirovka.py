class Sortirovka:

    def __int__(self):
        self.sorted = None

    def sortirovka(self, val):
        if isinstance(val, list) or isinstance(val, tuple):
            self.do_sortirovka(val)
        else:
            raise TypeError("Non sortable strukture")

    def do_sortirovka(self, val):
        n = len(val)
        a = list(val)

        q = type(a[0])
        for item in a:
            if type(item) is not q:
                raise TypeError("Different values in strukture")

        for i in range(n - 1):
            for j in range(n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]

        if isinstance(val, tuple):
            a = tuple(a)

        self.sorted = a
        print(a)

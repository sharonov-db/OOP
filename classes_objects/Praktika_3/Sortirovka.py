class Sortirovka:

    def __int__(self):
        self.sorted = None

    def sortirovka(self, val):
        def __do_sortirovka(val):
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
            return a

        if isinstance(val, list) or isinstance(val, tuple):
            return __do_sortirovka(val)
        else:
            raise TypeError("Non sortable strukture")



class Sortirovka:

    def __int__(self):
        self.sorted = []

    def sortirovka(self, *args):

        if not isinstance(args[0], list):
            raise TypeError("Non sortable value")
        else:
            a = list(args[0])

        if not isinstance(args[0], tuple):
            raise TypeError("Non sortable value")
        else:
            a = tuple(args[0])

        n = len(a)

        q = type(a[0])
        for item in a:
            if type(item) is not q:
                raise TypeError("Different values in strukture")

        for i in range(n - 1):
            for j in range(n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]

        self.sorted = a

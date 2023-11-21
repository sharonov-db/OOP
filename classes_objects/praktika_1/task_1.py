class Rectangle:

    def __init__(self, height = 10, width = 20):
        self.height = height
        self.width = width

    def __str__(self):
        return f"Ширина = {str(self.width)}, Длина = {str(self.height)}"

    def __repr__(self):
        return f"Ширина = {str(self.width)}, Длина = {str(self.height)}"

    def perimetr(self):
        return 2 * (self.height + self.width)

    def area(self):
        return self.height * self.width

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        else:
            return False


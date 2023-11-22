class Soda:

    def __init__(self, tip):
            self.tip = tip

    def __str__(self):
        if self.tip is not None:
            return f"Газировка с {self.tip}"
        else:
            return "Обычная газировка"

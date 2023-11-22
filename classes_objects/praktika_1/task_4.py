class Soda:

    def __init__(self, tip):
            self.tip = tip

    def __str__(self):
        return self.get_tip()

    def get_tip(self):
        if self.tip is not None:
            return f"Газировка с {self.tip}"
        else:
            return "Обычная газировка"

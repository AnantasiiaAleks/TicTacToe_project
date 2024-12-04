class Cell:
    def __init__(self, number):
        self.number = number
        self.symbol = ' ' # Символ клетки ('X', 'O' или пробел)
        self.occupied = False # Статус занятости клетки
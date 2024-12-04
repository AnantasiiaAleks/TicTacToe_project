class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0 # Количество побед игрока


    def make_move(self):
        """Запрашивает ход игрока и проверяет корректность ввода."""
        while True:
            try:
                move = int(input(f'{self.name}, введите номер клетки для '
                                 f'вашего хода (1 - 9): '))
                if move < 1 or move > 9:
                    raise ValueError
                return move
            except ValueError:
                print('Неправильный ввод. Пожалуйста, введите '
                      'число от 1 до 9.')
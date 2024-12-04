import Cell


class Board:
    def __init__(self):
        self.cells = [Cell.Cell(i) for i in range(1, 10)] # Создаем 9 клеток для доски


    def display_board(self):
        """Отображает игровую доску."""
        print("-------------")
        for i in range(0, 9, 3):
            print(f'| {self.cells[i].symbol} | {self.cells[i + 1].symbol} \
             | {self.cells[i + 2].symbol} |')
            print("-------------")

    def change_cell(self, cell_number, symbol):
        """Изменяет символ клетки, если она не занята."""
        cell = self.cells[cell_number - 1]
        if cell.occupied:
            return False
        cell.symbol = symbol
        cell.occupied = True
        return True


    def check_game_over(self):
        """Проверяет, завершена ли игра (выигрыш или ничья)."""

        # Проверка строк, столбцов и диагоналей
        win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # горизонтальные линии
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # вертикальные линии
        (0, 4, 8), (2, 4, 6) # диагонали
        ]
        for pos in win_positions:
            if self.cells[pos[0]].symbol != " " and \
            self.cells[pos[0]].symbol == self.cells[pos[1]].symbol == \
            self.cells[pos[2]].symbol:
                return True
        return False


    def reset_board(self):
        """Сбрасывает игровую доску для новой игры."""

        for cell in self.cells:
            cell.symbol = ' '
            cell.occupied = False
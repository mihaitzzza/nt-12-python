def validate_value(decorated_function):
    def wrapper(*args, **kwargs):
        if args[1] not in ['x', 'o']:
            raise ValueError('Invalid value.')

        result = decorated_function(*args, **kwargs)

    return wrapper


class Cell:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    @validate_value
    def value(self, new_value):
        self._value = new_value


class Board:
    def __init__(self):
        self.configuration = [
            [Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell()]
        ]

    def _get_cell_value_or_index(self, cell, row, col):
        # 0 0 => 1 | 0 * 3 + 0 + 1 => 1
        # 0 1 => 2 | 0 * 3 + 1 + 1 => 2
        # 0 2 => 3 | 0 * 3 + 2 + 1 => 3
        # 1 0 => 4 | 1 * 3 + 0 + 1 => 4
        # 1 1 => 5 | 1 * 3 + 1 + 1 => 5
        # 1 2 => 6 | 1 * 3 + 2 + 1 => 6
        # 2 0 => 7 | 2 * 3 + 0 + 1 => 7
        # 2 1 => 8 | 2 * 3 + 1 + 1 => 8
        # 2 2 => 9 | 2 * 3 + 2 + 1 => 9
        if self.configuration[row][col].value is None:
            return str(row * 3 + col)

        return self.configuration[row][col].value

    def display(self):
        """Empty board configuration.
        +---+---+---+
        | 1 | 2 | 3 |
        +---+---+---+
        | 4 | 5 | 6 |
        +---+---+---+
        | 7 | 8 | 9 |
        +---+---+---+

        Configuration with data.
        +---+---+---+
        | x | 2 | o |
        +---+---+---+
        | 4 | x | 6 |
        +---+---+---+
        | 7 | 8 | o |
        +---+---+---+
        """
        print('+---+---+---+')
        for row_index, row in enumerate(self.configuration):
            cols_data = [
                self._get_cell_value_or_index(row[col_index], row_index, col_index)
                for col_index in range(3)
            ]
            joined_cols_data = ' | '.join(cols_data)

            print(f'| {joined_cols_data} |')
            print('+---+---+---+')

    def _get_winner_from_cells(self, cells):
        cells_data = {cell.value for cell in cells}
        if None in cells_data:
            return None

        if len(cells_data) == 1:
            return cells_data.pop()

        return None

    def check_winner(self):
        """"Checks if there is a winner using current board configuration.
        :returns - 'x' or 'o' if there's a winner, otherwise returns None
        """
        for row in self.configuration:
            winner = self._get_winner_from_cells(row)

            if winner:
                return winner

        for col in range(3):
            cells = [
                self.configuration[row][col]
                for row in range(3)
            ]

            winner = self._get_winner_from_cells(cells)

            if winner:
                return winner

        primary_diagonal_cells = [self.configuration[0][0], self.configuration[1][1], self.configuration[2][2]]
        winner = self._get_winner_from_cells(primary_diagonal_cells)
        if winner:
            return winner

        secondary_diagonal_cells = [self.configuration[2][0], self.configuration[1][1], self.configuration[0][2]]
        winner = self._get_winner_from_cells(secondary_diagonal_cells)
        return winner

    def get_available_moves(self):
        moves = []

        for row_index, row in enumerate(self.configuration):
            for col_index, cell in enumerate(row):
                if cell.value is None:
                    moves.append(row_index * 3 + col_index + 1)

        return moves

    def mark(self, player, position):
        position -= 1
        # 0 => 0 0
        # 1 => 0 1
        # 2 => 0 2
        # 3 => 1 0
        # 4 => 1 1
        # 5 => 1 2
        # position - 1
        row, col = (position // 3, position % 3)
        self.configuration[row][col].value = player

        return self.check_winner()

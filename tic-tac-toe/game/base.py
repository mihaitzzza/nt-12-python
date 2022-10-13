import random
from game.board import Board


class Game:
    def __init__(self):
        self.turn = 0
        self.winner = None
        self.player = random.choice(['x', 'o'])
        self.board = Board()

    def _get_user_input(self):
        available_moves = self.board.get_available_moves()

        while True:
            user_input = input(f'Available moves: {available_moves}. Player {self.player} choose your move: ')

            try:
                user_input = int(user_input)
            except ValueError:
                print('Option not available.')
                continue

            if user_input not in available_moves:  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
                print('Option not available.')
                continue

            return user_input

    def run(self):
        print('Play the game...')

        while self.turn < 9 and self.winner is None:
            print('Current board configuration:')
            self.board.display()

            user_input = self._get_user_input()

            self.winner = self.board.mark(self.player, user_input)
            if self.winner is not None:
                break

            self.player = 'x' if self.player == 'o' else 'o'
            self.turn += 1

        if self.winner:
            print(f'Player {self.winner} won the game!')
        else:
            print(f'Game ends as a draw.')

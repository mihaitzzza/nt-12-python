import pytest
from game.board import Board


@pytest.fixture
def board():
    return Board()


def test_board_is_initialized(board):
    for row in board.configuration:
        assert len(row) == 3

        for cell in row:
            assert cell.value is None

    assert len(board.configuration) == 3


def test_board_is_marked(monkeypatch, board):
    monkeypatch.setattr('game.board.Board.check_winner', lambda *args, **kwargs: None)

    board.mark('x', 1)

    assert board.configuration[0][0].value == 'x'


def test_check_winner(board):
    winner = board.mark('x', 3)
    assert winner is None

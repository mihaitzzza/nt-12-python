import pytest
from game.board import Cell


def test_cell_is_initialized():
    cell = Cell()
    assert cell.value is None


@pytest.mark.parametrize(("value", "exception"), (
        ('x', None),
        ('o', None),
        ('y', ValueError),
        (12, ValueError)
))
def test_set_cell_value(value, exception):
    cell = Cell()

    if exception is None:
        cell.value = value
        assert cell.value == value
    else:
        with pytest.raises(exception):
            cell.value = value

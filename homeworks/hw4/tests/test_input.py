import pytest

from homeworks.hw4.helpers import get_user_input
from homeworks.hw4.main import get_random_word


# @pytest.mark.parametrize(('mocked_user_input',), (
#     ('a',),
#     ('b',),
#     ('c',),
# ))
# def test_user_input(monkeypatch, mocked_user_input):
#     monkeypatch.setattr('builtins.input', lambda *args, **kwargs: mocked_user_input)
#
#     result = get_user_input([])
#     expected_result = mocked_user_input
#
#     assert expected_result == result


@pytest.fixture
def mocked_input(monkeypatch):
    def f(ch='a'):
        monkeypatch.setattr('builtins.input', lambda *args, **kwargs: ch)

    return f


@pytest.mark.parametrize(('user_characters',), (
        ('Cluj',),
        ('Craiova',),
        ('Bucuresti',),
))
def test_user_input(monkeypatch, user_characters, mocked_input):
    for ch in user_characters:
        # monkeypatch.setattr('builtins.input', lambda *args, **kwargs: ch)
        mocked_input(ch)

        result = get_user_input([])

        assert ch.lower() == result


def test_get_random_word(monkeypatch, mocked_input):
    # monkeypatch.setattr('random.choice', lambda *args, **kwargs: 'Cluj')
    monkeypatch.setattr('homeworks.hw4.main.random.choice', lambda *args, **kwargs: 'Cluj')
    assert get_random_word() == 'Cluj'

    # monkeypatch.setattr('builtins.input', lambda *args, **kwargs: 'a')
    mocked_input()
    user_input = get_user_input([])
    assert user_input == 'a'

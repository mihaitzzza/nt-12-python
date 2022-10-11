import pytest
from unit_tests.my_functions import my_sum, my_sum_from_all_args


@pytest.mark.parametrize(('a', 'b', 's'), (
        (5, 7, 12),
        (1, -2, -1),
        (0, 10, 10),
))
def test_my_sum(a, b, s):
    function_result = my_sum(a, b)

    assert function_result == s


@pytest.mark.parametrize(('function_args', 'function_kwargs', 'expected_result'), (
    ((1, 5, -3, 'abc', [12, 56, 'cad']), {}, 3),
    ((), {}, 0),
    ((2, 4, 'abc'), {'param_1': 2, 'param_2': 4, 'param_3': 5}, 6),
))
def test_my_sum_from_all_args(function_args, function_kwargs, expected_result):
    print('\n' * 2)
    print('function_params', function_args, function_kwargs)
    print('expected_result', expected_result)
    print('\n' * 2)
    # function_result = my_sum_from_all_args(1, 5, -3, 'abc', [12, 56, 'cad'])

    # my_sum_from_all_args((1, 5, -3, 'abc', [12, 56, 'cad']))  # we send only 1 parameter
    # function_result = my_sum_from_all_args(function_params)

    # my_sum_from_all_args(1, 5, -3, 'abc', [...])
    function_result = my_sum_from_all_args(*function_args, **function_kwargs)  # we send len(function_params) parameters
    # function_result = my_sum_from_all_args(..., param_1=2, param_2=4, param3=5)

    assert expected_result == function_result

# my_sum_from_all_args() == 0

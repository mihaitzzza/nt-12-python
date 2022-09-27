def get_divisors(n):
    divisors = []

    for number in range(2, n // 2 + 1):
        if n % number == 0:
            divisors.append(number)

    return divisors


def is_palindrome(n):
    str_value = str(n)
    str_value_reversed = str_value[::-1]
    return str_value == str_value_reversed

    # if str_value == str_value_reversed:
    #     return True
    # else:
    #     return False
    # if str_value == str_value_reversed:
    #     return True
    #
    # return False
    # return str_value == str_value_reversed

    # if str_value == str_value_reversed:
    #     _palindrome = True
    # else:
    #     _palindrome = False
    #
    # # return _palindrome
    # if _palindrome is True:
    #     return True
    # else:
    #     return False

    # return str_value == str_value_reversed


def get_user_input():
    while True:
        user_input = input('insert integer: ')

        # if user_input == 'exit' or user_input == 'quit':
        # if user_input.lower() == 'exit' or user_input.lower() == 'quit':  # ExIt => exit | EXIT => exit
        if user_input.lower() in ['exit', 'quit']:
            user_input = None
            break

        # user_input = int(user_input)  # user_input = "aaaa"
        # if user_input.isdigit()
        try:
            user_input = int(user_input)
        except ValueError:
            user_input = None

        if user_input is not None:
            break

    return user_input


def get_output(n):
    divisors = get_divisors(n)
    divisors_length = len(divisors)

    number_data = {
        'is_palindrome': is_palindrome(n),
        'is_prime': divisors_length == 0,
        'divisors': divisors,
        'max_divisor': max(divisors) if divisors_length > 0 else None,
        'digits': len(str(n))  # 12523 (5 digits)
    }

    return number_data

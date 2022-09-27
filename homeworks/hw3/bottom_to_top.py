def is_palindrome(n):
    str_value = str(n)
    str_value_reversed = str_value[::-1]
    return str_value == str_value_reversed


def is_prime(n):
    pass

def get_divisors(n):
    pass


if __name__ == '__main__':
    user_input = get_user_input()
    output = get_output(user_input)

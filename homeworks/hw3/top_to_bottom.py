def get_user_input():
    while True:
        user_input = input("insert integer")

        if user_input == 'exit' or user_input == 'quit':
            break

        try:
            user_input = int(user_input)
            break
        except:
            continue

    return user_input


def is_palindrome(n):
    pass


def get_output(user_input):
    return {
        "is_palindrome": is_palindrome(user_input),  # False
        "is_prime": True,  # False
        "divisors": [],
        "max_divisor": None,  # or max divisor, of course
    }


if __name__ == '__main__':
    user_input = get_user_input()
    if type(user_input) == int:
        my_dict = get_output(user_input)
        print('my_dict', my_dict)

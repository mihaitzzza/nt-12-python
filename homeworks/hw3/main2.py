if __name__ == '__main__':
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

    if type(user_input) == int:
        divisors = []
        for number in range(2, user_input // 2 + 1):
            if user_input % number == 0:
                divisors.append(number)
        divisors_length = len(divisors)

        str_value = str(user_input)
        str_value_reversed = str_value[::-1]
        is_palindrome = str_value == str_value_reversed

        number_data = {
            'is_palindrome': user_input,
            'is_prime': divisors_length == 0,
            'divisors': divisors,
            'max_divisor': max(divisors) if divisors_length > 0 else None
        }

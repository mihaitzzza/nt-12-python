from utils import get_user_input, get_output

if __name__ == '__main__':
    user_input = get_user_input()

    if user_input is not None:
        number_data = get_output(user_input)
    else:
        print('User did not inserted a number.')

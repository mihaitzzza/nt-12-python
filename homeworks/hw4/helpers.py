import string


def get_user_input(used_chars):
    while True:
        user_input = input('your character: ')

        if user_input in string.ascii_letters and len(user_input) == 1 and user_input not in used_chars:
            return user_input.lower()


def get_hashed_word(word, used_chars):
    # hashed_word = []
    #
    # for ch in word:
    #     if ch.lower() in used_chars:
    #         hashed_word.append(ch)
    #     else:
    #         hashed_word.append('*')
    #
    # return ''.join(hashed_word)

    # using list comprehension
    hashed_chars_list = [
        ch if ch.lower() in used_chars else '_'
        for ch in word
    ]
    return ''.join(hashed_chars_list)

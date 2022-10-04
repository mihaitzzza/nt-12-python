import random
from constants import words, max_lives
from helpers import get_user_input, get_hashed_word

if __name__ == '__main__':
    random_word = random.choice(words)
    lives = max_lives

    print('random_word', random_word)
    used_chars = set()
    word_chars = set(list(random_word.lower()))

    while lives > 0 and not word_chars.issubset(used_chars):
        hashed_word = get_hashed_word(random_word, used_chars)
        print('hashed_word', hashed_word)

        user_input = get_user_input(used_chars)
        used_chars.add(user_input)

        if user_input not in word_chars:
            lives -= 1

    if lives == 0:
        print('You lost! The word was:', random_word)
    else:
        print('You won! The word was:', random_word)

# # MAP FUNCTION
# # def my_function(n):
# #     return n ** 2
# #     # return n % 5 == 0
#
#
# numbers = range(10)
# print('numbers', list(numbers))
#
# # mapped_numbers = []
# # for number in numbers:
# #     mapped_numbers.append(number ** 2)
# # print('mapped_numbers', mapped_numbers)
#
# # mapped_numbers = map(my_function, numbers)
# mapped_numbers = map(lambda n: n ** 2, numbers)
# print('mapped_numbers', list(mapped_numbers))

# # FILTER FUNCTION
# # numbers = range(10)
# # print('numbers', list(numbers))
# # filtered_numbers = []
# # for number in numbers:
# #     if number % 2 == 0:
# #         filtered_numbers.append(number)
# # print('filtered_numbers', filtered_numbers)
#
# # def my_function(n):
# #     return n % 2 == 0
#
# numbers = range(10)
# print('numbers', list(numbers))
#
# # filtered_numbers = filter(my_function, numbers)
# filtered_numbers = filter(lambda n: n % 2 == 0, numbers)
# print('filtered_numbers', list(filtered_numbers))

# # FILTER + MAP FUNCTIONS
# numbers = range(10)
# print('numbers', list(numbers))
#
# # x = []
# # for n in numbers:
# #     if n % 2 == 0:
# #         x.append(n ** 2)
# # print('x', x)
# filtered_numbers = filter(lambda n: n % 2 == 0, numbers)
# # print('filtered_numbers', list(filtered_numbers))
#
# mapped_numbers = map(lambda n: n ** 2, filtered_numbers)
# print('mapped_numbers', list(mapped_numbers))

# # LIST COMPREHENSION
# numbers = range(10)
# print('numbers', list(numbers))
#
# # updated_list = [n for n in numbers]
# # updated_list = [n ** 2 for n in numbers]
# # updated_list = [n for n in numbers if n % 2 == 0]
# updated_list = [
#     n ** 2
#     for n in numbers
#     if n % 2 == 0
# ]
# print('updated_list', updated_list)


# # ZIP FUNCTION
# # import itertools
# #
# # numbers = range(10)
# # print('numbers', list(numbers))
# #
# # letters = ['a', 'b', 'c', 'd', 'e']
# # print('letters', letters)
# #
# # zip_result = zip(numbers, letters)
# # print('zip_result', list(zip_result))
#
# # zip_longest_result = itertools.zip_longest(letters, numbers)
# # print('zip_longest_result', list(zip_longest_result))
#
# # my_dict_from_zip = dict(zip_result)
# # print('my_dict_from_zip', my_dict_from_zip)
# #
# # my_dict_from_zip_longest = dict(zip_longest_result)
# # print('my_dict_from_zip_longest', my_dict_from_zip_longest)
#
# numbers = range(10)
# print('numbers', list(numbers))
#
# letters = ['a', 'b', 'c', 'd', 'e']
# print('letters', letters)
#
# random_stuff = ['A', 'B', 'C']
#
# zip_result = zip(numbers, letters, random_stuff)
# # [(0, 'a'), (1, 'b'), (2, 'c'), ...]
#
# # my_dict = dict(zip(letters, numbers))
# # my_dict = dict(zip_result)
# # print('my_dict', my_dict)
#
# # my_dict = dict(
# #     [
# #         (letter, number)
# #         for number, letter in zip_result
# #     ]
# # )
# # my_dict = {
# #     letter: number
# #     for number, letter in zip_result
# # }
# # print('my_dict', my_dict)
#
# print('zip_result', list(zip_result))


# GENERATORS
import sys

my_range = range(10)


# my_numbers = list(my_range)
# # # print('my_numbers in bytes', sys.getsizeof(my_numbers), sys.getsizeof(my_numbers) * 10 ** -6)
# for n in my_numbers:
#     print(n)

# def generate_numbers():  # generators uses "yield"
#     for n in my_range:
#         yield n
#
#
# numbers_generator = generate_numbers()
# # print('numbers_generator', numbers_generator)
# # print('numbers_generator', sys.getsizeof(numbers_generator), sys.getsizeof(numbers_generator) * 10 ** -6)
# for n in numbers_generator:
#     print(n)
#
# print(len(numbers_generator))

# def generate_numbers():
#     value = 1
#     prev = 0
#
#     while True:
#         yield value
#
#         old_prev = prev
#         prev = value
#         value += old_prev
#
#
# numbers_generator = generate_numbers()
# # 1, 1, 2, 3, 5, 8, 13, 21, ...
#
# # Print first 100 from Fibonacci series.
# for i in range(100):
#     print(next(numbers_generator))

def generate_numbers():
    n = 0

    while n < 10:
        yield n
        n += 1


numbers_generator = generate_numbers()

for i in range(100):
    try:
        print(next(numbers_generator))
    except StopIteration:
        break

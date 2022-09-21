# # my_age = 15
# #
# # # if my_age >= 18:
# # #     print('Instr. 1: Persoana este adulta.')
# # #     print('Instr. 2: Persoana este adulta.')
# # # else:
# # #     if my_age >= 14:
# # #         print('Instr. 1: Persoana este minora, dar are buletin!')
# # #     else:
# # #         print('Instr. 1: Persoana este minora! Persoana nu are buletin.')
# #
# # if my_age >= 18:
# #     print('Instr. 2: Persoana este adulta.')
# # elif my_age >= 14:
# #     print('Instr. 1: Persoana este minora, dar are buletin!')
# # elif my_age >= 10:
# #     print('fa ceva...')
# # else:
# #     print('Instr. 1: Persoana este minora! Persoana nu are buletin.')
# #
# # print('End of program')
#
# # print('before while')
# #
# # index = 0
# # while index < 10:
# #     print('inside while', index)
# #     index += 1
# #
# # print('after while')
#
# # print('before for')
#
# # for element in [1, 2, 3]:
# # for number in range(0, 5, 2):  # range(start, stop, step)
# # for my_tuple in enumerate(['a', 'b', 'c', 'd']):
# #     # print('my_tuple', my_tuple)
# #     index, element = my_tuple  # index = my_tuple[0]; element = my_tuple[1]
# #     print(f'{index + 1}: {element}')
# # for index, element in enumerate(['a', 'b', 'c', 'd']):
# #     print(f'{index + 1}: {element}')
# #
# # print('after for')
#
# # while True:
# #     print('infinite loop')
# #     break
# #
# # print('after while')
#
# for element in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     if element % 2 == 0:
#         continue
#
#     print(element)
#
# print('after for')

# def a():
#     print('I am function a!')
#
#
# a()

# def my_sum(a, b):
#     # print('5 + 7 =', 5 + 7)
#     print(f'{a} + {b} = {a + b}')
#     # return a + b
#
#
# # print('result', my_sum(1, 5))
#
# # print(my_sum(1, 2))

# def my_function(param_1, param_2, optional_param_1='abc', optional_param_2=None):
#     print(param_1, param_2, optional_param_1, optional_param_2)
#
#
# # my_function(20, 10)
# # my_function(20, 10, 'aaa')
# # my_function(20, 10, optional_param_2=100)
# # my_function(param_2=20, param_1=10, optional_param_2=100)
#
# my_function(1, 2, 3, 4, 5)
# my_function(1, 2, 3, 4, 5, 7, 8, 9, 10, 11)

# *args = positional variable-length arguments
# **kwargs = optional variable-length arguments
def my_function(param_1, param_2, *args, optional_param_1='abc', optional_param_2=None, **kwargs):
    print(param_1, param_2, args, optional_param_1, optional_param_2, kwargs)


#
#
# my_function(1, 2, 3, 4, 5)
# my_function(1, 2, 3, 4, 5, 7, 8, 9, 10, 11)
# my_function(1, 2, 3, 4, 5, 7, 8, 9, 10, 11, a=1, b=2, c=3, d=4, e=5)

# def my_function(*args, **kwargs):
#     return args[0] + args[1]

# my_function()
# my_function(1)
# my_function(a=1)
# my_function(a=1, b=2)
# my_function('a', 'b', 'c', a=1, b=2)

# print(my_function(1, 6))

# def my_function():
#     print('inside my function')
#     # ...
#     # ...
#     my_function()
#     # ...
#     # ...
#
#
# my_function()


# n = 5 => return 5 + my_sum(4) => return 5 + 10 (15)
# n = 4 => return 4 + my_sum(3) => return 4 + 6 (10)
# n = 3 => return 3 + my_sum(2) => return 3 + 3 (6)
# n = 2 => return 2 + my_sum(1) => return 2 + 1 (3)
# n = 1 => return 1 + my_sum(0) => return 1 + 0 (1)
# n = 0 => return 0
# def my_sum(n):
#     if n == 0:
#         return 0
#
#     return n + my_sum(n - 1)
#
#
# sum_ = my_sum(5)  # 0 + 1 + 2 + 3 + 4 + 5 = 15 = (5 * 6) / 2
# print('sum', sum_)  # prints 15
#
# # def a():
# #     return  # this will return None
# #     print('a')

# user_input = input('Insert whatever you want: ')
# print('user_input', user_input, type(user_input))


# a = int(input('a = '))
# b = int(input('b = '))
# print('sum = ', a + b)

# try:
#     a = int(input('a = '))
#     print('a is a number!')
#     print('b', b)
# except ValueError:
#     print('a is not a number!')
# except NameError:
#     print('you used a invalid variable')

# print('b', b)  # NameError

# try:
#     a = int(input('a = '))
#     print('a is a number!')
#     # print('b', b)
# except (ValueError, NameError) as e:
#     print('exception', e, type(e))
#     if type(e) == NameError:
#         print('invalid variable')
#     else:
#         print('a is not a number')
# else:
#     print('ELSE BRANCH!')
# finally:
#     print('FINALLY BRANCH!')


# my_list = [1, 32, 3242]
# list_length = len(my_list)
#
# print(len(my_list))  # print(list_length)
# for index in range(0, len(my_list), 2):  # for index in range(0, list_length,2):
#     print('index', index)
#
# # len(my_list)  # list_length
# # len(my_list)  # list_length
# # len(my_list)  # list_length
# # len(my_list)  # list_length

# def f():
#     print('this is a function!')
#
# f()

# (lambda *args, **kwargs: print('this is a lambda function!'))()
# f()

# my_students = [{
#     'name': 'Popescu Ion',
#     'grade': 7.00
# }, {
#     'name': 'Ionut George',
#     'grade': 4.50
# }, {
#     'name': 'Dan Ionel',
#     'grade': 10.00
# }]
#
# # def sort_by_function(student):
# #     return student["grade"]
#
#
# my_students.sort(key=lambda student: student["grade"], reverse=True)
#
# print('my_students', my_students)

# x = int(input('>'))
# print('x', x)
#
# # if x % 2 == 0:
# #     my_string = 'even'
# # else:
# #     my_string = 'odd'
# my_string = 'even' if x % 2 == 0 else 'odd'
#
# print('my_string', my_string)

# def f(n):
#     # if n % 2 == 0:
#     #     return 'even'
#     # else:
#     #     return 'odd'
#     if n % 2 == 0:
#         return 'even'
#
#     return 'odd'

# my_list = [2, 7]
#
#
# def f():
#     a = 2
#     b = 7
#     my_list = "something else"
#     print(a + b, my_list)
#
#
# f()
# print(my_list)

# my_list = [1, 2, 3]
#
#
# def f(my_list):
#     print('my_list', my_list)
#
#
# f(['a', 'b'])


# my_list = [1, 2, 3, ['a', 'b', 'c']]
#
#
# def f(a):
#     # a = a[:]
#     a = a.copy()
#     a.append(4)
#     a[3].append('d')
#     print('a', a)
#
#
# f(my_list)
# print('my_list', my_list)

# def f1():
#     def f2():
#         # a = 20
#         print('this is f2', a)
#         # print('---', dir(f1))
#
#     # a = 10
#
#     f2()
#     print('this is f1', a)
#
#
# a = 30
#
# f1()
# print('this is main.py', a)


# from .my_functions import f
# from basics.my_functions import f, my_list
# from basics.my_functions import *
# import basics.my_functions
# from basics.my_functions import *
# from basics.my_variables import *
# from basics.my_package.my_functions import f, my_list as f_my_list, my_string as f_my_string
# from basics.my_package.my_variables import my_list, my_string as v_my_string
from basics.my_package import f, f_my_list, v_my_list, f_my_string, v_my_string
# import basics.my_functions as x
# import random
# import math

# my_string = 'GLOBAL OVERWRITE!'

if __name__ == '__main__':
    # print('inside my_script.py', __name__, basics.my_functions.f(2, 5))
    # print('inside my_script.py', __name__, basics.my_functions.my_list)
    # print('inside my_script.py', __name__, basics.my_functions.my_string)
    print('inside my_script.py', __name__, f(2, 5))
    print('inside my_script.py', __name__, f_my_list, v_my_list)
    print('inside my_script.py', __name__, f_my_string, v_my_string)

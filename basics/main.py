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



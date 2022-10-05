# # def my_sum(a, b):
# #     return a + b
# #
# #
# # def another_function(my_function):
# #     # print('my_function', my_function)
# #     r = my_function(5, 7)
# #     print('r', r)
# #
# #
# # def get_my_sum_function():
# #     return my_sum
# #
# #
# # if __name__ == '__main__':
# #     # r = my_sum(5, 7)
# #     # print('r', r)
# #     # another_function(my_sum)
# #     # a_function = get_my_sum_function()
# #     # r = a_function(5, 7)
# #     # print('r', r)
# #     a_function = my_sum
# #     # r = a_function(5, 7)
# #     # print('r', r)
# #     x = my_sum(5, 7)
#
#
# from my_sum import my_sum, my_triple_sum
#
#
# if __name__ == '__main__':
#     # my_decorated_function = my_decorator(my_sum)
#     # r = my_decorated_function(5, 7)
#     # print('r =', r)
#     decorated_result = my_sum(5, 7)
#     print('decorated_result =', decorated_result)
#     print('my function name', my_sum.__name__)
#     print('my function doc', my_sum.__doc__)
#
#     original_result = my_sum.__wrapped__(5, 7)
#     print('original_result =', original_result)
#
#     my_triple_result = my_triple_sum(1, 2, 3)
#     print('my_triple_result', my_triple_result)

# from my_functions import get_csv_data, my_sum
#
# if __name__ == '__main__':
#     # data = get_csv_data()
#     r = my_sum(5, 7)


from my_functions import my_decorator_with_params, my_sum

if __name__ == '__main__':
    # my_decorated_function = my_decorator_with_params(3)(my_sum)
    # r = my_decorated_function(1, 1)
    # print('r', r)
    # r = my_sum(1, 1)
    # print('r', r)

    my_pows = range(3)
    for i in my_pows:
        my_decorated_function = my_decorator_with_params(i)(my_sum)
        r = my_decorated_function(1, 1)
        print('r', r)

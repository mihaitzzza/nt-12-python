# from functools import wraps
#
#
# def my_decorator(my_function):
#     @wraps(my_function)
#     def wrapper(*args, **kwargs):
#         result = my_function(*args, **kwargs)
#         return result ** 2
#
#     return wrapper
#
#
# @my_decorator
# def my_sum(a, b):
#     """
#     This function returns sum of two numbers.
#     @param a - This is themy_execution_decorator first number.
#     @param b - This is the second number.
#     @returns - The sum of a & b
#     """
#     return a + b
#
#
# @my_decorator
# def my_triple_sum(a, b, c):
#     return a + b + c

# import csv
# import time
#
#
# def my_execution_decorator(decorated_function):
#     def wrapper(*args, **kwargs):
#         start_time = time.time() * 1000
#         result = decorated_function(*args, **kwargs)
#         end_time = time.time() * 1000
#
#         print(f'{decorated_function.__name__} execution time:', end_time - start_time)
#
#         return result
#
#     return wrapper
#
#
# @my_execution_decorator
# def get_csv_data():
#     with open('/home/mihaitzzza/Downloads/worldcities.csv') as csv_file:
#         data = []
#         csv_dict_reader = csv.DictReader(csv_file)
#         for my_dict in csv_dict_reader:
#             data.append(my_dict)
#
#     return data
#
#
# @my_execution_decorator
# def my_sum(a, b):
#     """
#     This function returns sum of two numbers.
#     @param a - This is the first number.
#     @param b - This is the second number.
#     @returns - The sum of a & b
#     """
#     return a + b


from functools import wraps


# def my_decorator(my_function):
#     @wraps(my_function)
#     def wrapper(*args, **kwargs):
#         result = my_function(*args, **kwargs)
#         return result ** 2
#
#     return wrapper
def my_decorator_with_params(pow_number):
    def my_decorator(my_decorated_function):
        def wrapper(a, b):
            result = my_decorated_function(a, b)
            return result ** pow_number

        return wrapper

    return my_decorator


@my_decorator_with_params(10)
def my_sum(a, b):
    """
    This function returns sum of two numbers.
    @param a - This is the first number.
    @param b - This is the second number.
    @returns - The sum of a & b
    """
    return a + b

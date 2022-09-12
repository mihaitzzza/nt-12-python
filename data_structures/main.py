# # my_list = [1, 3.5, (3 + 2j), True, False, None, 'some random string', [1, 2, 3]]
# # #          0   1      2       3      4     5             6                7 (len(my_list) - 1)
# # #         -8  -7     -6      -5     -4    -3            -2               -1
# #
# # # print(my_list)
# # # print(type(my_list))
# # # print(my_list[6])
# # # print(len(my_list))
# # print(my_list[-3], my_list[-2])
#
# # empty_list = []
# # list_with_duplicates = [1, 1, 1, 1]
#
# # my_list = []
# # print('my_list with length:', my_list, len(my_list))
# #
# # my_list.append(24)
# # print('my_list with length:', my_list, len(my_list))
# #
# # my_list.append(-30)
# # print('my_list with length:', my_list, len(my_list))
# #
# # # print(my_list[200])  # this will result in an exception (error)
# #
# # my_list[0] = 100
# # print('my_list with length:', my_list, len(my_list))
#
# # list_1 = [1, 2, 3]
# # list_2 = [1, 2, 3]
# # print(list_1 is list_2, list_1 == list_2)
#
# # list_1 = [1, 2, 3]
# # list_2 = list_1
# # # print(list_1 is list_2, list_1 == list_2)
# #
# # list_1.append(4)
# # print(list_1, list_2)
#
# # list_1 = [1, 2, 3]
# # list_2 = [1, 2, 3]
# # print(list_1, list_2)
# #
# # list_1.append(4)
# # print(list_1, list_2)
#
# # list_1 = [1, 2, 3]
# # list_2 = [2, 3, 4]
# # list_3 = list_1 + list_2
# # print('list_3', list_3)
#
# # SLICE - list_name[start:stop:step] <=> list_name[0:len(list_name):1]
# list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #         0  1  2  3  4  5  6  7  8  9
# # print(list_1[5])
# # print(list_1[::], list_1[0:len(list_name):1])
# # print(list_1[5:])
# # print(list_1[5:7])  # => [list_1[5], list_1[6]]
# # print(list_1[1:8:2])
# # print(list_1[-3:])
# print(list_1[::-1])

# my_tuple = (10, 20, 30, 40, 50)
# my_empty_tuple = tuple()  # my_tuple = ()  # this is an empty tuple
# print('my_empty_tuple', my_empty_tuple, type(my_empty_tuple))
#            0   1   2   3   4
#           -5  -4  -3  -2  -1
# print(my_tuple, type(my_tuple), my_tuple[1:3])
# print(my_tuple[4])

# my_list = []  # this is an empty list
# my_list = list()
# print(my_list, type(my_list))


# my_tuple = (10, 20, 30, 40, 50)
# my_tuple_copy = my_tuple
# print('my_tuple', my_tuple, type(my_tuple), id(my_tuple), id(my_tuple_copy))
#
# my_list = list(my_tuple)
# # print('my_list', my_list, type(my_list))
#
# my_list.append(60)
# my_list.append(70)
# # print('my_list', my_list)
#
# my_tuple = tuple(my_list)
# print('my_tuple', my_tuple, type(my_tuple), id(my_tuple), id(my_tuple_copy))

# my_empty_dict = {}
# print('my_empty_dict', my_empty_dict, type(my_empty_dict))

# my_empty_dict = dict()
# print('my_empty_dict', my_empty_dict, type(my_empty_dict))

# my_dict = {
#     'a': 2,
#     'b': 'dan',
#     'c': [1, 2, 3],
#     'd': (1, 2, 3),
#     0: 'ana are mere',
# }
# print('my_dict', my_dict)
# print(my_dict['c'])
# print(my_dict[0])

# my_data = {
#     0: "ana",
#     1: "are",
#     2: "mere"
# }
# print(my_data[0])
# print(my_data[1])
# print(my_data[2])

# my_dict = {
#     'first_name': 'Mihai',
#     'last_name': 'Popescu',
#     'age': 18,
# }
# print('my_dict', my_dict)
# # print(my_dict['last_name'])
#
# my_dict['age'] = 20
#
# print('my_dict', my_dict)
#
# my_dict['city'] = 'Craiova'
#
# print('my_dict', my_dict)

# my_dict = {
#     'a': 10,
#     'a': 20
# }
#
# print('my_dict', my_dict)

# my_dict = {
#     'a': 10
# }
# print(my_dict['a'])
#
# del my_dict['a']
#
# print(my_dict['a'])

# .keys() / .items() / .values()
# my_dict = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }

# print(my_dict.keys())
# print(my_dict.items())
# print(my_dict.values())

# my_dict = {
#     "fname": "mihai",
#     "lname": "popescu",
#     "age": 23
# }
#
# print(my_dict)
#
# del my_dict['age']
#
# print(my_dict)

# my_list = [{'a': 1, 'b': 2, 'c': [(0, 1), 1, 2, 3, {}]}]

# my_dict = {
#     [1, 2, 3]: 'a'
# }
#
# print('my_dict', my_dict)

# my_set = {}
# my_set = set()
# print('my_set', my_set, type(my_set))

# my_set = {1, 2, 3, 5, 5, 5, 5}
# print('my_set', my_set, type(my_set))
#
# my_set.add(6)
# print('my_set', my_set, type(my_set))
#
# my_set.remove(3)
# print('my_set', my_set, type(my_set))
#
# my_set.pop()
# print('my_set', my_set, type(my_set))


romana = [
    {
        'name': 'popescu ion',
    },
    {
        'name': 'dobre george',
    }
]

mate = [
    {
        'name': 'dobre george',
    }
]

set_romana = {'popescu ion', 'dobre george'}
set_mate = {'dobre george'}
set_geo = {'vasile ionut'}

# intersection = set_romana.intersection(set_mate).intersection(set_geo)
# print('intersection', intersection)
# print(len(intersection))

# print(set_romana - set_mate)

# print(set_mate.issubset(set_romana))
# print(set_romana.issuperset(set_mate))

# print('a' in 'i learn python')

my_list = [1, 2, 3]
print(1 in my_list, 'a' in my_list)

my_tuple = (1, 2, 3)
print(1 in my_tuple, 'a' in my_tuple)

my_set = {1, 2, 3}
print(1 in my_set, 'a' in my_set)

my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
# print(1 in my_dict, 'a' in my_dict)
# print(1 in my_dict.keys(), 'a' in my_dict.keys())
print(1 in my_dict.values(), 'a' in my_dict.values())

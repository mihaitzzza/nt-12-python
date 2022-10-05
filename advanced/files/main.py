# import csv
#
# if __name__ == '__main__':
#     # with open('example.txt') as file:  # /home/mihaitzzza/work/siit/nt-12-python/advanced/files/example.txt
#     #     # print(file.readlines())
#     #     for index, line_content in enumerate(file.readlines()):
#     #         line_content = line_content.replace("\n", "")
#     #         print(f'On line {index + 1} we have: {line_content}')  # each line ends in '\n'
#
#     # with open('example.txt', 'w') as file:
#     #     file.write('something else...')
#
#     # with open('example.txt', 'a') as file:
#     #     file.write('\nsomething else...')
#
#     # with open('example.csv') as file:
#     #     for index, line in enumerate(file.readlines()):
#     #         print(line)
#
#     # with open('example.csv') as csv_file:
#     #     data = []
#     #     csv_reader = csv.reader(csv_file)
#     #
#     #     for index, row in enumerate(csv_reader):
#     #         if index == 0:
#     #             header = row
#     #         else:
#     #             data.append(row)
#     #             # data.append(
#     #             #     {
#     #             #         key: value
#     #             #         for key, value in zip(header, row)
#     #             #     }
#     #             # )
#     #
#     # print('header', header)
#     # print('data', data)
#     #
#     # my_countries = [
#     #     # dict(zip(header, row))
#     #     {key: value for key, value in zip(header, row)}
#     #     for row in data
#     # ]
#     #
#     # print('my_countries', my_countries)
#
#     # with open('example.csv') as csv_file:
#     #     csv_reader = csv.DictReader(csv_file)
#     #     for data in csv_reader:
#     #         print('data', data)
#
#     # data = [
#     #     ['name', 'color'],
#     #     ['apple', 'red'],
#     #     ['pear', 'yellow'],
#     # ]
#     # with open('output.csv', 'w') as csv_file:
#     #     csv_writer = csv.writer(csv_file)
#     #     # for row in data:
#     #     #     csv_writer.writerow(row)
#     #     csv_writer.writerows(data)
#
#     # data = [
#     #     {
#     #         "first_name": "mihai",
#     #         "age": 10
#     #     },
#     #     {
#     #         "first_name": "popescu",
#     #         "age": 12
#     #     },
#     #     {
#     #         "first_name": "ionel",
#     #         "age": 15
#     #     }
#     # ]
#     # with open('output_dict.csv', 'w') as csv_file:
#     #     csv_dict_writer = csv.DictWriter(csv_file, fieldnames=list(data[0].keys()))
#     #     csv_dict_writer.writeheader()
#     #     csv_dict_writer.writerows(data)
#
#     data = [
#         {
#             "first_name": "second attempt 1",
#             "age": 10
#         },
#         {
#             "first_name": "second attempt 2",
#             "age": 12
#         },
#         {
#             "first_name": "second attempt 3",
#             "age": 15
#         }
#     ]
#     with open('output_dict.csv', 'a') as csv_file:
#         csv_dict_writer = csv.DictWriter(csv_file, fieldnames=list(data[0].keys()))
#         csv_dict_writer.writerows(data)

# import csv
# import sys
#
# if __name__ == '__main__':
#     # with open('/home/mihaitzzza/Downloads/worldcities.csv') as csv_file:
#     #     data = []
#     #     csv_reader = csv.reader(csv_file)
#     #     for row in csv_reader:
#     #         data.append(row)
#     #
#     # for i in range(3):
#     #     print(data[i])
#     #
#     # print('data size in MB', sys.getsizeof(data) * 10 ** -6)
#
#     def generate_csv_content():
#         with open('/home/mihaitzzza/Downloads/worldcities.csv') as csv_file:
#             csv_reader = csv.reader(csv_file)
#             for row in csv_reader:
#                 yield row
#
#
#     csv_content = generate_csv_content()
#     for i in range(3):
#         print(next(csv_content))
#
#     print('data size in MB', sys.getsizeof(csv_content) * 10 ** -6)

import json

if __name__ == '__main__':
    with open('input.json') as json_file:
        data = json.load(json_file)

    print('data', data)

    with open('output.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

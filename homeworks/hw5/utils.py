import csv
import json
import uuid


def get_input(file_path):
    data = []

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)

        for index, row in enumerate(csv_reader):
            if index == 0:
                header = ['id']
                header.extend(row)
            else:
                # car_data = [index]
                car_data = [str(uuid.uuid4())]
                car_data.extend(row)
                data.append(car_data)

    return header, data


def parse_to_json(header, data):
    return [
        dict(zip(header, car_data))
        for car_data in data
    ]


def write_to_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)


# def get_cars_by_power(cars, min_=0, max_=999999999999):
#     return [
#         car
#         for car in cars
#         if min_ <= int(car['hp']) < max_
#     ]

def get_cars_by_criteria(cars, key=None, min_=0, max_=None):
    def check(car):
        hp = int(car[key])

        condition = min_ <= hp

        if max_ is not None:
            condition = condition and hp < max_

        return condition

    if key is None:
        raise ValueError('key parameter should is mandatory')

    return [
        car
        for car in cars
        if check(car)
    ]


def get_cars_by_brand(cars):
    """
    Get cars by brand, e.g.:
    {
        'opel': [...],
        'bmw': [...],
        'dacia': [...],
    }
    """
    brands = set([
        car['brand']
        for car in cars
    ])

    output = {}
    for brand in brands:
        output[brand] = [
            car
            for car in cars
            if car['brand'] == brand
        ]

    return output

import os
import shutil

from utils import get_input, parse_to_json, get_cars_by_criteria, write_to_json, get_cars_by_brand
from constants import OUTPUT_FOLDER_NAME, CAR_CATEGORY_FILE_NAMES

if __name__ == '__main__':
    header, data = get_input('input.csv')
    data = parse_to_json(header, data)

    try:
        shutil.rmtree(os.path.join(OUTPUT_FOLDER_NAME))
    except Exception:
        pass
    os.makedirs(os.path.join(OUTPUT_FOLDER_NAME), exist_ok=True)

    slow_cars = get_cars_by_criteria(data, key='hp', max_=120)
    fast_cars = get_cars_by_criteria(data, key='hp', min_=120, max_=180)
    sport_cars = get_cars_by_criteria(data, key='hp', min_=180)

    cheap_cars = get_cars_by_criteria(data, key='price', max_=1000)
    medium_cars = get_cars_by_criteria(data, key='price', min_=1000, max_=5000)
    expensive_cars = get_cars_by_criteria(data, key='price', min_=5000)

    cars = [
        slow_cars,
        fast_cars,
        sport_cars,
        cheap_cars,
        medium_cars,
        expensive_cars
    ]
    for file_name, car_set in zip(CAR_CATEGORY_FILE_NAMES, cars):
        write_to_json(os.path.join(OUTPUT_FOLDER_NAME, file_name), car_set)

    cars_by_brand = get_cars_by_brand(data)
    for brand, car_set in cars_by_brand.items():
        write_to_json(os.path.join(OUTPUT_FOLDER_NAME, f'{brand}.json'), car_set)

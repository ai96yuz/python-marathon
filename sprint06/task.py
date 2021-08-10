# Task 1


import json


def find(file, key):
    with open(file) as f:
        content = json.load(f)

    result_list = []
    if isinstance(content, list):
        dict_result = {k: v for element in content for k, v in element.items()}
        return result_list if not dict_result.get(key) else {k: v for element in content for k, v in
                                                             element.items()}.get(key)
    else:
        password = content.get(key)
        if isinstance(password, list):
            return password
        else:
            return [password]


# Task 2


import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('root')
logger.setLevel(logging.ERROR)


def parse_user(output_file, *input_files):
    all_data = []
    for file_name in input_files:
        try:
            with open(file_name, 'r') as f:
                all_data.extend(json.load(f))
        except FileNotFoundError:
            logger.error(f'File {file_name} doesn\'t exists')
    if all_data:
        all_data.pop(-1)
    with open(output_file, 'w') as outfile:
        json.dump(all_data, outfile)
    return output_file


def print_file(output_file):
    with open(output_file, 'r') as f:
        if output_file == 'app.log':
            print(f.read())
        else:
            json_file = json.load(f)
            print(json.dumps(json_file, indent = 4))


# Task 3


import json
import jsonschema
from jsonschema import validate
import csv


def user_with_department(csv_file, user_json, department_json):
    pass


def validate_json(data, schema):
    pass
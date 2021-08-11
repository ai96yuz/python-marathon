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


# Task 4


import json


class Student:
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def __str__(self):
        return '{} ({}): {}'.format(self.full_name, self.avg_rank, self.courses)

    @classmethod
    def from_json(cls, json_file):
        with open(json_file) as f:
            student_data = json.load(f)
        return '{} ({}): {}'.format(student_data.get('full_name'), student_data.get('avg_rank'), student_data.get('courses'))


class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    def __str__(self):
        students = [str(Student(**item)) for item in self.students]
        return f'{self.title}: {students}'

    @classmethod
    def create_group_from_file(cls, students_file):
        with open(students_file) as f:
            stud_data = json.load(f)
        if not isinstance(stud_data, list):
            stud_data = [stud_data]
        return cls(students_file.split('.')[0], stud_data)

    @classmethod
    def serialize_to_json(cls, list_of_groups, filename):
        result_list = []
        for el in list_of_groups:
            result_dict = {'title': el.title, 'students': el.students}
            result_list.append(result_dict)
        with open(filename, 'a') as f:
            json.dump(result_list, f)

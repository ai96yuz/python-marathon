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



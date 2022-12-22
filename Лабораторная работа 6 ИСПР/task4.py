import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',') -> list[dict]:
    with open(filename, 'r') as f:
        headers = f.readline()[:-1].split(delimiter)
        return [dict(zip(headers, line[:-1].split(delimiter))) for line in f]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

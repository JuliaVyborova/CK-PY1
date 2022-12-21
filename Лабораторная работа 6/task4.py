import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    list_dict = []  # Пустой список словарей, куда будет все записываться

    with open(filename, 'r') as f:
        file_data = f.readlines()  # Считать содержимое файла

        for i in range(len(file_data)):  # Разделить строки на списки и удалить разделители строк
            file_data[i] = file_data[i].replace(new_line, '').split(delimiter)

        headers = file_data[0]  # Выделить список заголовков
        rows = file_data[1:]  # Выделить списки списков данных
        for row in rows:
            list_dict.append(dict(zip(headers, row)))

    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

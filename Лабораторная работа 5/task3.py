import random


def get_unique_list_numbers() -> list[int]:
    list_ = []  # создаем пустой список для записи случайных чисел
    for i in range(16):
        number = random.randint(-10, 10)  # генерируем число
        if number not in list_:  # проверяем уникальность числа
            list_.append(number)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

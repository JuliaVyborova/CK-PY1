from random import randint


def get_unique_list_numbers(left_border=-10, right_border=10, length=15) -> list[int]:
    list_ = []  # создаем пустой список для записи случайных чисел
    while len(list_) != length:
        number = randint(left_border, right_border)  # генерируем число
        if number not in list_:  # проверяем уникальность числа
            list_.append(number)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

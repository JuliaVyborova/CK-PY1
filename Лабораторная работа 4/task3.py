# def delete(list_, index=None):
#     if index is None or index == -1:  # по умолчанию удаляется последний элемент из списка
#         index = -1
#         return list_[:index]
#     elif index != -1:  # удаляем с любым заданным индексом кроме -1
#         return list_[:index] + list_[index + 1:]


def delete(list_, index=-1):
    if index != -1:  # удаляем символ с любым индексом кроме индекса по умолчанию
        return list_[:index] + list_[index + 1:]
    else:
        return list_[:index]


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
print(delete([0, 1, 2], index=-1))  # [0, 1]  # для самопроверки
print(delete([0, 1, 2], index=-2))  # [0, 2]  # для самопроверки

money_capital = 20000  # финансовая подушка безопасности
salary = 5000  # ежемесечная зарплата
spend = 6000  # ежемесячные расходы  на проживание (превышают зарплату)
increase = 0.05  # процент увеличения расходов со второго месяца

month = 0  # количество месяцев, которое можно прожить
delta = 0  # нехватка средств

# так как заранее не известно заданное количество шагов (нам нужно его найти)
# то лучше использовать цикл с условием

# мой вариант кода:
while delta < money_capital:
    delta = spend - salary
    money_capital -= delta
    spend *= 1 + increase
    month += 1

# while True:
#     delta = spend - salary
#     if delta > money_capital:
#         break
#
#     month += 1
#     money_capital -= delta
#     spend *= 1 + increase

print(month)  # 8

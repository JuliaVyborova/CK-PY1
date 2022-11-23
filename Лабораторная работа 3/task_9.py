salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for number in range(months):  # перебираем каждый месяц
    delta = spend - salary  # недостаток средств
    money_capital += delta  # формируем подушку безопасности
    spend *= 1 + increase  # учитываем повышение цен

print(round(money_capital))

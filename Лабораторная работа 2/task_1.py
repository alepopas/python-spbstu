money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count_months = 0

while True:
    money_capital = salary + money_capital - spend
    if money_capital < 0:
        break
    count_months += 1
    spend *= 1 + increase


print("Количество месяцев, которое можно протянуть без долгов:", count_months)

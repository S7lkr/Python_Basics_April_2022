vacation_money = float(input())
saved_money = float(input())

days = 0
days_spend = 0

while saved_money < vacation_money and days_spend < 5:
    act = input()
    amount = float(input())
    days += 1
    if act == 'spend':
        saved_money -= amount
        days_spend += 1
        if saved_money < 0:
            saved_money = 0
    elif act == 'save':
        saved_money += amount
        days_spend = 0

if days_spend == 5:
    print('You can\'t save the money.')
    print(days)

if saved_money >= vacation_money:
    print(f'You saved the money for {days} days.')

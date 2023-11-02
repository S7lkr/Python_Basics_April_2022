age = int(input())
washer_price = float(input())
price_toy = int(input())

birthday_money = 0
toys = 0

for num in range(1, age + 1):
    if num % 2 == 0:
        birthday_money += ((num / 2) * 10) - 1
    else:
        toys += 1

money_toys = toys * price_toy
total_money = birthday_money + money_toys
money_left = abs(total_money - washer_price)

if total_money >= washer_price:
    print(f'Yes! {money_left:.2f}')
else:
    print(f'No! {money_left:.2f}')
group_budget = int(input())
season = input()
fisher_count = int(input())

price = 0
discount = 0
second_discount = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if fisher_count <= 6:
    discount = 0.1
elif 7 <= fisher_count <= 11:
    discount = 0.15
elif fisher_count >= 12:
    discount = 0.25

new_price = price - (price * discount)
money_left = abs(group_budget - new_price)

if fisher_count % 2 == 0 and season != 'Autumn':
    second_discount = 0.05
    new_price -= (new_price * second_discount)
    money_left = abs(group_budget - new_price)

if group_budget >= new_price:
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    print(f'Not enough money! You need {money_left:.2f} leva.')

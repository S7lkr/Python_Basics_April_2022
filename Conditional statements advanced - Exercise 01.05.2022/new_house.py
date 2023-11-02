flower = input()
flower_count = int(input())
budget = int(input())

price_per_flower = 0
discount = 0

if flower == 'Roses':
    price_per_flower = 5
    if flower_count > 80:
        discount = 0.1
elif flower == 'Dahlias':
    price_per_flower = 3.80
    if flower_count > 90:
        discount = 0.15
elif flower == 'Tulips':
    price_per_flower = 2.80
    if flower_count > 80:
        discount = 0.15
elif flower == 'Narcissus':
    price_per_flower = 3
    if flower_count < 120:
        # NOTE: Discount is NEGATIVE because we add it to the raw price via
        # double minus that will become + in the formula:
        # price raw - (-discount) = price raw + discount
        discount = -0.15
elif flower == 'Gladiolus':
    price_per_flower = 2.50
    if flower_count < 80:
        discount = -0.2

price_raw = flower_count * price_per_flower
price_total = price_raw - (discount * price_raw)
money_left = abs(budget - price_total)

if price_total <= budget:
    print(f'Hey, you have a great garden with {flower_count} {flower} and {money_left:.2f} leva left.')
else:
    print(f'Not enough money, you need {money_left:.2f} leva more.')
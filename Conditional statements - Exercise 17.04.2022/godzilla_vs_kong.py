film_budget = float(input())
n_statists = int(input())
outfit_price = float(input())

# Decor price costs 10% of the overall film budget
decor = 0.10 * film_budget
outfit_price *= n_statists

if n_statists > 150:
    outfit_discount = outfit_price * 0.10
    outfit_price -= outfit_discount

# Money LEFT or NEEDED. We take the absolute (always positive) value
money_needed_or_left = abs((decor + outfit_price) - film_budget)

if (decor + outfit_price) > film_budget:
    print('Not enough money!')
    print(f'Wingard needs {money_needed_or_left:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {money_needed_or_left:.02f} leva left.')

budget = float(input())
season = input()

destination = ''
place = ''
budget_percent = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        budget_percent = 0.30
        place = 'Camp'
    elif season == 'winter':
        budget_percent = 0.70
        place = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        budget_percent = 0.40
        place = 'Camp'
    elif season == 'winter':
        budget_percent = 0.8
        place = 'Hotel'
else:
    destination = 'Europe'
    budget_percent = 0.9
    place = 'Hotel'

price = budget * budget_percent

print(f'Somewhere in {destination}')
print(f'{place} - {price:.2f}')

budget = float(input())
category = input()
people_in_group = int(input())

ticket_price = 0
money_left = 0

if category == 'VIP':
    ticket_price = 499.99
elif category == 'Normal':
    ticket_price = 249.99

if 1 <= people_in_group <= 4:
    budget -= budget * 0.75
elif 5 <= people_in_group <= 9:
    budget -= budget * 0.6
elif 10 <= people_in_group <= 24:
    budget -= budget * 0.5
elif 25 <= people_in_group <= 49:
    budget -= budget * 0.4
else:
    budget -= budget * 0.25

money_for_tickets = ticket_price * people_in_group
money_left = abs(budget - money_for_tickets)

if budget >= money_for_tickets:
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    print(f'Not enough money! You need {money_left:.2f} leva.')
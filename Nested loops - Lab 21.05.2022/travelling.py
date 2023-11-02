total_money_saved = 0
journey_ended = False

while not journey_ended:
    destination = input()
    if destination == 'End':
        journey_ended = True
        break
    money_for_travel = float(input())
    while total_money_saved < money_for_travel:
        income = float(input())
        total_money_saved += income
        continue
    total_money_saved = 0
    print(f'Going to {destination}!')

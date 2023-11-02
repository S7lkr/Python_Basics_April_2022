sea_holidays = int(input())
mountain_holidays = int(input())

money_earned = 0
sea_cnt = sea_holidays
mountain_cnt = mountain_holidays

while sea_cnt > 0 or mountain_cnt > 0:
    type = input()
    if type == 'Stop':
        break
    if type == 'sea':
        if sea_cnt > 0:
            money_earned += 680
            sea_cnt -= 1
    elif type == 'mountain':
        if mountain_cnt > 0:
            money_earned += 499
            mountain_cnt -= 1
else:
    print('Good job! Everything is sold.')

print(f'Profit: {money_earned} leva.')
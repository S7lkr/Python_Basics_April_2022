tournament_days = int(input())

total_amount = 0
amount = 0

total_wins = 0
total_loses = 0
day_wins_cnt = 0
day_loses_cnt = 0

for d in range(1, tournament_days+1):
    sport = input()
    while sport != 'Finish':
        result = input()
        if result == 'win':
            amount += 20
            day_wins_cnt += 1
        elif result == 'lose':
            day_loses_cnt += 1
        sport = input()
    else:
        if day_wins_cnt > day_loses_cnt:
            amount += amount * 0.1

        total_amount += amount
        amount = 0
        total_wins += day_wins_cnt
        total_loses += day_loses_cnt
        day_wins_cnt = 0
        day_loses_cnt = 0

if total_wins > total_loses:
    total_amount += total_amount * 0.2
    print(f'You won the tournament! Total raised money: {total_amount:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_amount:.2f}')
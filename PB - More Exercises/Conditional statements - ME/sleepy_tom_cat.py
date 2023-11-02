free_days = int(input())

free_days_game = free_days * 127
working_days_game = (365 - free_days) * 63
total_game = free_days_game + working_days_game

diff = abs(30000 - total_game)
hours = diff // 60
minutes = diff % 60

if total_game < 30000:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
import math

competitions = int(input())
start_points = int(input())

competitions_wined = 0
total_gained_points = 0

for _ in range(competitions):
    title = input()
    if title == 'W':
        total_gained_points += 2000
        competitions_wined += 1
    elif title == 'F':
        total_gained_points += 1200
    elif title == 'SF':
        total_gained_points += 720

total_gained_points += start_points
average_points = (total_gained_points - start_points) / competitions
winning_percent = (competitions_wined / competitions) * 100

print(f'Final points: {total_gained_points}')
print(f'Average points: {math.floor(average_points)}')
print(f'{winning_percent:.2f}%')
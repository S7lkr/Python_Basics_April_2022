from math import ceil

days = int(input())
km_first_day = float(input())

total_distance = km_first_day
daily_distance = km_first_day

for d in range(1, days+1):
    percents = int(input()) / 100
    daily_distance += daily_distance * percents
    total_distance += daily_distance

diff = abs(total_distance - 1000)

if total_distance >= 1000:
    print(f'You\'ve done a great job running {ceil(diff)} more kilometers!')
else:
    print(f'Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers')
minutes_walk = int(input())
walks_day = int(input())
calories_taken_day = int(input())

burned_cal_day = minutes_walk * walks_day * 5

if burned_cal_day >= (calories_taken_day / 2):
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned_cal_day}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burned_cal_day}.')
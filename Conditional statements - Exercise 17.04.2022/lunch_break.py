from math import ceil
chapter = input()
chapter_duration = int(input())
break_time = int(input())

lunch_time = 0.125 * break_time
rest_time = 0.25 * break_time

# Time LEFT ONLY for the movie, after the lunch and rest have passed
time_left_for_movie = break_time - (lunch_time + rest_time)
time_bonus = time_left_for_movie - chapter_duration

if chapter_duration <= time_left_for_movie:
    print(f'You have enough time to watch {chapter} and left with {ceil(time_bonus)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {chapter}, you need {ceil(abs(time_bonus))} more minutes.')

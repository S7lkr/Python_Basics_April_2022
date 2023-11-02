a = int(input())

day_of_week = ''

if 1 <= a <= 7:
    if a == 1:
        day_of_week = 'Monday'
    elif a == 2:
        day_of_week = 'Tuesday'
    elif a == 3:
        day_of_week = 'Wednesday'
    elif a == 4:
        day_of_week = 'Thursday'
    elif a == 5:
        day_of_week = 'Friday'
    elif a == 6:
        day_of_week = 'Saturday'
    else:
        day_of_week = 'Sunday'
    print(day_of_week)
else:
    print('Error')

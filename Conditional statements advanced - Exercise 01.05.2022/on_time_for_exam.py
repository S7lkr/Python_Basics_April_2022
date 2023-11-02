exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

# Here we transform the standard clock time 'hh:mm' into minutes (for both, exam & arrival times):
# 2.15PM -> (2h * 60) + 15 = 135 min total
exam_total_time = (exam_hour * 60) + exam_minutes
arrival_total_time = (arrival_hour * 60) + arrival_minutes
# If the exam is in 10.30, and we arrive in 10.15, time_diff will be 15min (positive)
time_diff = abs(exam_total_time - arrival_total_time)

# Before we start we will see ALL the different possibilities:
# 1) Late: 1.1 late with more than hour -> hh:mm
#          1.2 late within an hour
# 2) A little early OR on time:
#          2.1 exactly on time
#          2.2 earlier with no more than 30min
# 3) Too EARLY (more than 30min):
#          3.1 more than an hour -> hh:mm
#          3.2 less than hour but more than 30 min (from 31 to 59 min) -> only minutes

# If we are late -> 2 options: 1 to 59 min OR
if arrival_total_time > exam_total_time:
    # If the latency is more than 59 min, we are late with at least 1 hour
    if time_diff >= 60:
        hours_late = time_diff // 60
        minutes_late = time_diff % 60
        print('Late')
        print(f'{hours_late}:{minutes_late:02d} hours after the start')
    # Else we are late only with minutes. NOTE this can be not more than 59 min!!
    else:
        print('Late')
        print(f'{time_diff} minutes after the start')
# If we are ON TIME or EARLIER with 30 min or less than 30 min
elif arrival_total_time <= exam_total_time and time_diff <= 30:
    # If the arrival time is before the exam time with less than a 30 min, we are on time
    print('On time')
    # ONLY here we are from 1 to 29 min earlier
    if time_diff > 0:
        print(f'{time_diff} minutes before the start')
# ELSE, only if we are MORE THAN 30 min earlier
else:
    print('Early')

    # More than an hour later
    if time_diff >= 60:
        hours_earlier = time_diff // 60
        minutes_earlier = time_diff % 60
        print(f'{hours_earlier}:{minutes_earlier:02d} hours before the start')
    else:
        print(f'{time_diff} minutes before the start')
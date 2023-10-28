time_first = int(input())
time_second = int(input())
time_third = int(input())

# Total time in seconds
total_time = time_first + time_second + time_third

# Here we represent 'total_time', by showing ONLY the minutes number: 110 sec -> 1:... min
total_minutes = total_time // 60
# Here we represent 'total_time', by showing ONLY the seconds number: 110 sec -> ...:50 min
total_seconds = total_time % 60

# IMPORTANT NOTE: We only play with the seconds in the IF section. Why?
# Because only in the seconds there is a LEADING ZERO and there are only 2 possible variants: with OR without it
# For example: 10:05 -> leading zero;   10:15 -> no leading zero

# if total_seconds < 10:
#     # There is need of a leading zero for the seconds number, like: ...:07 or ...:02 for example
#     print(f'{total_minutes}:0{total_seconds}')
# else:
#     # There is no need of a leading zero in the seconds tab: ...:28, ...:54 etc.
#     print(f'{total_minutes}:{total_seconds}')

print(f'{total_minutes}:{total_seconds:02d}')

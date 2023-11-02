from math import floor

l = float(input())
w = float(input())

length_cm = l * 100
width_cm = (w - 1) * 100

rows = floor(width_cm / 70)
columns = floor(length_cm / 120)

working_places_cnt = (rows * columns) - 3
print(round(working_places_cnt))

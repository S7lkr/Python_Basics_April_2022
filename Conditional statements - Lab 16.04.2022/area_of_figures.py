figure_type = input()
area = 0
from math import pi

if figure_type == 'square':
    a = float(input())
    area = a * a
elif figure_type == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
elif figure_type == "circle":
    r = float(input())
    area = pi * (r ** 2)
elif figure_type == 'triangle':
    a = float(input())
    h = float(input())
    area = 0.5 * (a * h)

print(f'{area:.3f}')
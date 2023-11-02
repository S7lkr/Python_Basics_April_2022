house_height = float(input())
house_length = float(input())
ceil_height = float(input())

house_area = ((house_height * house_length - 2.25) * 2) + ((house_height ** 2) * 2) - 2.4
ceil_area = 2 * (house_height * house_length) + (ceil_height * house_height)

green_paint_l = house_area / 3.4
red_paint_l = ceil_area / 4.3

print(f'{green_paint_l:.2f}')
print(f'{red_paint_l:.2f}')
from math import ceil
from math import floor

box_num = int(input())
roll_num = int(input())
price_for_one_gloves = float(input())
price_for_brush = float(input())

gloves_num = ceil(0.35 * roll_num)
brush_num = floor(0.48 * box_num)

box_price = box_num * 21.50
roll_price = roll_num * 5.20

gloves_price = gloves_num * price_for_one_gloves
brush_price = brush_num * price_for_brush

all_costs = box_price + roll_price + gloves_price + brush_price
delivery = all_costs / 15

print(f'This delivery will cost {delivery:.2f} lv.')
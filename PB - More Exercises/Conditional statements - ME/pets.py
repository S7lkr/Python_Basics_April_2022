from math import floor
from math import ceil

days = int(input())
food_kg_left = int(input())
kg_food_dog = float(input())
kg_food_cat = float(input())
gr_food_turtle = float(input())

kg_food_dog *= days
kg_food_cat *= days
gr_food_turtle *= days / 1000

total_food_eaten = kg_food_dog + kg_food_cat + gr_food_turtle
food_left_needed = abs(food_kg_left - total_food_eaten)

if food_kg_left >= total_food_eaten:
    print(f'{floor(food_left_needed)} kilos of food left.')
else:
    print(f'{ceil(food_left_needed)} more kilos of food are needed.')
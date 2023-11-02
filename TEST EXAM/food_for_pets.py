days = int(input())
food = float(input())


total_food_dog = 0
total_food_cat = 0
total_food_eaten_day = 0
biscuits_eaten = 0

for d in range(1, days+1):
    food_eaten_by_dog = int(input())
    food_eaten_by_cat = int(input())

    total_food_dog += food_eaten_by_dog
    total_food_cat += food_eaten_by_cat
    total_food_eaten_day += food_eaten_by_dog + food_eaten_by_cat
    if d % 3 == 0:
        biscuits_eaten += total_food_eaten_day * 0.1
    total_food_eaten_day = 0

total_food_eaten = total_food_dog + total_food_cat
average_food_eaten = (total_food_eaten / food) * 100
average_dog = (total_food_dog / total_food_eaten) * 100
average_cat = (total_food_cat / total_food_eaten) * 100

print(f'Total eaten biscuits: {round(biscuits_eaten)}gr.')
print(f'{average_food_eaten:.2f}% of the food has been eaten.')
print(f'{average_dog:.2f}% eaten from the dog.')
print(f'{average_cat:.2f}% eaten from the cat.')
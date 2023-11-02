chicken_menu_number = int(input())
fish_menu_number = int(input())
vegetarian_menu_number = int(input())

group_menu = (chicken_menu_number * 10.35) + (fish_menu_number * 12.40) + (vegetarian_menu_number * 8.15)
dessert = group_menu * 0.20
price = dessert + group_menu
final_price = price + 2.50

print(f'{final_price:.2f}')

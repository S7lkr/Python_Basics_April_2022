fruit = input()
set_option = input()
n_sets = int(input())

price_for_1_set = 0

if set_option == 'small':
    if fruit == 'Watermelon':
        price_for_1_set = 2 * 56
    elif fruit == 'Mango':
        price_for_1_set = 2 * 36.66
    elif fruit == 'Pineapple':
        price_for_1_set = 2 * 42.1
    elif fruit == 'Raspberry':
        price_for_1_set = 2 * 20
elif set_option == 'big':
    if fruit == 'Watermelon':
        price_for_1_set = 5 * 28.7
    elif fruit == 'Mango':
        price_for_1_set = 5 * 19.6
    elif fruit == 'Pineapple':
        price_for_1_set = 5 * 24.8
    elif fruit == 'Raspberry':
        price_for_1_set = 5 * 15.2

price_all_sets = price_for_1_set * n_sets

if 400 <= price_all_sets <= 1000:
    price_all_sets -= price_all_sets * 0.15
elif price_all_sets > 1000:
    price_all_sets -= price_all_sets / 2

print(f'{price_all_sets:.2f} lv.')
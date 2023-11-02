month = input()
overnight_count = int(input())

# Normal prices for 1 overnight
price_apartment = 0
price_studio = 0
# The amount of the discount. If price is 50 and discount is 20%, the new value will be 10lv off -> 50 *0.2 = 10lv
bonus_apartment = 0
bonus_studio = 0

if month == 'May' or month == 'October':
    price_apartment = 65
    price_studio = 50
    if overnight_count > 14:
        bonus_studio = price_studio * 0.3
    elif 7 < overnight_count <= 13:
        bonus_studio = price_studio * 0.05
elif month == 'June' or month == 'September':
    price_apartment = 68.7
    price_studio = 75.2
    if overnight_count > 14:
        bonus_studio = price_studio * 0.2
elif month == 'July' or month == 'August':
    price_apartment = 77
    price_studio = 76

if overnight_count > 14:
    bonus_apartment = price_apartment * 0.1

price_apartment_total = price_apartment - bonus_apartment
price_apartment_total *= overnight_count
price_studio_total = price_studio - bonus_studio
price_studio_total *= overnight_count

print(f'Apartment: {price_apartment_total:.2f} lv.')
print(f'Studio: {price_studio_total:.2f} lv.')
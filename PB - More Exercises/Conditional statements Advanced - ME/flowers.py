chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

price_ch = 0
price_r = 0
price_t = 0

if season == 'Spring' or season == 'Summer':
    price_ch = chrysanthemums * 2
    price_r = roses * 4.1
    price_t = tulips * 2.5
if season == 'Autumn' or season == 'Winter':
    price_ch = chrysanthemums * 3.75
    price_r = roses * 4.5
    price_t = tulips * 4.15

money_paid = price_ch + price_t + price_r

if holiday == 'Y':
    money_paid += money_paid * 0.15
if tulips > 7 and season == 'Spring':
    money_paid -= money_paid * 0.05
if roses >= 10 and season == 'Winter':
    money_paid -= money_paid * 0.1
if (chrysanthemums + roses + tulips) > 20:
    money_paid -= money_paid * 0.2

money_paid += 2
print(f'{money_paid:.2f}')
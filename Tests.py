# # All prime numbers from 1 to n
n = int(input())

for num in range(1, n+1):
    if num > 1:
        for div in range(2, num):
            if num % div == 0:
                break
        else:
            print(num, end=' ')

for i in range(97, 100):
    print(chr(98), end='')


# Text length
text = input()
for ch in range(0, len(text)):
    print(ord('a'))

n = int(input())
discount = int(input()) / 100

n -= (n * discount)       # 100 = 100 - (100 * 0.1)
b = n * discount

print(n)
print(b)


while True:
    text = input()
    if text == 'Stop':
        break
    print(text)


locations_cnt = int(input())

total_gold_per_day = 0
average_gold_per_day = 0

for i in range(1, locations_cnt+1):
    expected_gold_for_day = float(input())
    days = int(input())
    for d in range(1, days+1):
        gold_extracted_for_day = float(input())
        total_gold_per_day += gold_extracted_for_day
        if d == days:
            average_gold_per_day = total_gold_per_day / days
            if average_gold_per_day >= expected_gold_for_day:
                total_gold_per_day = 0
                print(f'Good job! Average gold per day: {average_gold_per_day:.2f}.')
                break
            else:
                gold_needed = abs(expected_gold_for_day - average_gold_per_day)
                print(f'You need {gold_needed:.2f} gold.')

age = input()

adults = 0
children = 0
toys_price = 0
sweater_price = 0

while age != 'Christmas':
    age = int(age)
    if age <= 16:
        children += 1
        toys_price += 5
    else:
        adults += 1
        sweater_price += 15
    age = input()

print(f"Number of adults: {adults}")
print(f"Number of kids: {children}")
print(f"Money for toys: {toys_price}")
print(f"Money for sweaters: {sweater_price}")


team = input()
souvenir = input()
souvenir_cnt = int(input())
price = 0

if team == 'Argentina':
    if souvenir == 'flags':
        price = souvenir_cnt * 3.25
    elif souvenir == 'caps':
        price = souvenir_cnt * 7.2
    elif souvenir == 'posters':
        price = souvenir_cnt * 5.1
    elif souvenir == 'stickers':
        price = souvenir_cnt * 1.25
elif team == 'Brazil':
    if souvenir == 'flags':
        price = souvenir_cnt * 4.2
    elif souvenir == 'caps':
        price = souvenir_cnt * 8.5
    elif souvenir == 'posters':
        price = souvenir_cnt * 5.35
    elif souvenir == 'stickers':
        price = souvenir_cnt * 1.2
elif team == 'Croatia':
    if souvenir == 'flags':
        price = souvenir_cnt * 2.75
    elif souvenir == 'caps':
        price = souvenir_cnt * 6.9
    elif souvenir == 'posters':
        price = souvenir_cnt * 4.95
    elif souvenir == 'stickers':
        price = souvenir_cnt * 1.1
elif team == 'Denmark':
    if souvenir == 'flags':
        price = souvenir_cnt * 3.1
    elif souvenir == 'caps':
        price = souvenir_cnt * 6.5
    elif souvenir == 'posters':
        price = souvenir_cnt * 4.8
    elif souvenir == 'stickers':
        price = souvenir_cnt * 0.9

if (team == 'Argentina' or team == 'Brazil' or team == 'Croatia' or team == 'Denmark')\
        and (souvenir == 'flags' or souvenir == 'caps' or souvenir == 'posters' or souvenir == 'stickers'):
    print(f'Pepi bought {souvenir_cnt} {souvenir} of {team} for {price:.2f} lv.')

elif team != 'Argentina' and team != 'Brazil' and team != 'Croatia' and team != 'Denmark':
    print('Invalid country!')

elif souvenir != 'flags' and souvenir != 'caps' and souvenir != 'posters' and souvenir != 'stickers':
    print('Invalid stock!')

cat_cnt = int(input())
small_cats = 0
big_cats = 0
large_cats = 0
food_eaten = 0

for cat in range(1, cat_cnt+1):
    food_gr = float(input())

    if 100 <= food_gr < 200:
        small_cats += 1
    elif 200 <= food_gr < 300:
        big_cats += 1
    elif 300 <= food_gr < 400:
        large_cats += 1

    food_eaten += food_gr

total_price = (food_eaten / 1000) * 12.45

print(f'Group 1: {small_cats} cats.')
print(f'Group 2: {big_cats} cats.')
print(f'Group 3: {large_cats} cats.')

print(f'Price for food per day: {total_price:.2f} lv.')
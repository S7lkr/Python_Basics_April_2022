from math import floor
from math import ceil

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
present_price = float(input())

money_earned = (magnolias * 3.25) + (hyacinths * 4) + (roses * 3.5) + (cactus * 8)
money_earned -= money_earned * 0.05
money_left_needed = abs(money_earned - present_price)

if money_earned >= present_price:
    print(f'She is left with {floor(money_left_needed)} leva.')
else:
    print(f'She will have to borrow {ceil(money_left_needed)} leva.')
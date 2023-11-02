juniors = int(input())
seniors = int(input())
track = input()

price_j = 0
price_s = 0

if track == 'trail':
    price_j = juniors * 5.5
    price_s = seniors * 7
elif track == 'cross-country':
    if (juniors + seniors) >= 50:
        price_j = juniors * (8 * 0.75)
        price_s = seniors * (9.5 * 0.75)
    else:
        price_j = juniors * 8
        price_s = seniors * 9.5
elif track == 'downhill':
    price_j = juniors * 12.25
    price_s = seniors * 13.75
elif track == 'road':
    price_j = juniors * 20
    price_s = seniors * 21.5

total_price = price_j + price_s
total_price -= total_price * 0.05

print(f'{total_price:.2f}')
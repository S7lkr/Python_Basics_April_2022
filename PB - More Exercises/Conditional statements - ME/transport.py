n = int(input())
time = input()

price = 0

if n >= 100:
    price = 0.06 * n
elif n >= 20:
    price = 0.09 * n
else:
    if time == 'day':
        price = n * 0.79 + 0.7
    elif time == 'night':
        price = n * 0.9 + 0.7

print(f'{price:.2f}')
n_1lv = int(input())
n_2lv = int(input())
n_5lv = int(input())
amount = int(input())

for a in range(n_1lv+1):
    for b in range(n_2lv+1):
        for c in range(0, n_5lv+1):
            if (a * 1) + (b * 2) + (c * 5) == amount:
                print(f'{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {amount} lv.')
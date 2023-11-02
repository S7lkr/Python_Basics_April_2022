n = int(input())

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if n % (a+b) == 0 and n % (c+d) == 0 and (a+b) == (c+d):
                    lucky_number = f'{a}{b}{c}{d}'
                    print(lucky_number, end=' ')
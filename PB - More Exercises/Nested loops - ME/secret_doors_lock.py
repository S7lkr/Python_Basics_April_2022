n1 = int(input())
n2 = int(input())
n3 = int(input())

for a in range(1, n1+1):
    if a % 2 == 0:
        for b in range(1, n2+1):
            if b > 1:
                for div in range(2, b):
                    if b % div == 0:
                        break
                else:
                    for c in range(1, n3+1):
                        combination = f'{a} {b} {c}'
                        if c % 2 == 0:
                            print(combination)
print()
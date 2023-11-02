n1 = int(input())
n2 = int(input())
n3 = int(input())

for a in range(1, n1+1):
    for b in range(2, n2+1):
        for c in range(1, n3+1):
            if a % 2 == 0 and c % 2 == 0:
                for div in range(2, b):
                    if b % div == 0:
                        break
                else:
                    print(f'{a} {b} {c}')
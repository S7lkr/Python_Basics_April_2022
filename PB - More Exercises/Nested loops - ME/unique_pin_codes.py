n1_limit = int(input())
n2_limit = int(input())
n3_limit = int(input())

for a in range(1, n1_limit+1):
    for b in range(1, n2_limit+1):
        if b > 1:
            for div in range(2, b):
                if b % div == 0:
                    break
            else:
                for c in range(1, n3_limit+1):
                    if a % 2 == 0 and c % 2 == 0:
                        print(a, b, c)
print()

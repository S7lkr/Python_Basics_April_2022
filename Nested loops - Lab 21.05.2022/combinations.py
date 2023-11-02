n = int(input())
combinations = 0

for x1 in range(n + 1):
    for x2 in range(n + 1):
        for x3 in range(n + 1):
            result = x1 + x2 + x3
            if result == n:
                combinations += 1
print(combinations)

n = int(input())
result = 0

for num in range(1, n+1):
    number = int(input())
    result += number
print(f'{result/n:.2f}')
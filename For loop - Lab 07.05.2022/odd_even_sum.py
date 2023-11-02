n = int(input())

even_sum = 0
odd_sum = 0

for i in range(n):
    current_num = int(input())
    if i % 2 == 0:
        odd_sum += current_num
    else:
        even_sum += current_num

if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    diff = abs(even_sum - odd_sum)
    print('No')
    print(f'Diff = {diff}')
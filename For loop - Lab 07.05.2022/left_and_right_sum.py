number = int(input())

left_sum = 0
right_sum = 0
diff = 0

for i in range(number):
    n1 = int(input())
    left_sum += n1

for h in range(number):
    n2 = int(input())
    right_sum += n2

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')
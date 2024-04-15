# Prime/Non-prime with Divs
n = int(input())
div_cnt = 0
is_prime = True

for div in range(2, n):
    if n % div == 0:
        div_cnt += 1
if div_cnt != 0:
    print(f'Number {n} is non-prime. It has a total of {div_cnt+2} dividers.')
else:
    print('Number is prime.')
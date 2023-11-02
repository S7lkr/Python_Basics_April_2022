import sys

n = int(input())
suma = 0
max_num = -sys.maxsize

for i in range(n):
    c_n = int(input())
    suma += c_n
    if c_n > max_num:
        max_num = c_n

suma -= max_num
diff = abs(suma - max_num)

if max_num == suma:
    print('Yes')
    print(f'Sum = {suma}')
else:
    print('No')
    print(f'Diff = {diff}')
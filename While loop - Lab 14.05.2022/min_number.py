import sys

num = input()
min_number = sys.maxsize

while num != 'Stop':
    num = int(num)
    if num < min_number:
        min_number = num
    num = input()
print(min_number)
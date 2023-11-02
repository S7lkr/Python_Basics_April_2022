import sys

num = input()
max_number = -sys.maxsize

while num != 'Stop':
    num = int(num)
    if num > max_number:
        max_number = num
    num = input()
print(max_number)
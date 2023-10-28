a = int(input())

if a < 10:
    if a >= 0:
        if a % 2 == 0:
            print(f'{a} is a positive, even number and lesser than 10 ')
        else:
            print(f'{a} is a positive, odd number and lesser than 10')
    elif a < 0:
        if a % 2 == 0:
            print(f'{a} is a negative, even number lesser than 10')
        else:
            print(f'{a} is a negative, odd number lesser than 10')
elif 10 <= a <= 20:
    if a % 2 == 0:
        print(f'{a} is even number between 10 and 20')
    else:
        print(f'{a} is odd number between 10 and 20')
else:
    if a % 2 != 0:
        print(f'{a} is odd number greater than 20')
    else:
        print(f'{a} is even number greater than 20')
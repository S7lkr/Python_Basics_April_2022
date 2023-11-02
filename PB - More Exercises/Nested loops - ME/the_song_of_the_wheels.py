number = int(input())

password_cnt = 0
the_password_is = ''
password_found = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if b > a and c > d and (a*b + c*d) == number:
                    print(f'{a}{b}{c}{d}', end=' ')
                    password_cnt += 1
                    if password_cnt == 4:
                        password_found = True
                        the_password_is = f'{a}{b}{c}{d}'
                    elif password_cnt < 4:
                        break
if password_found:
    print()
    print(f'Password: {the_password_is}')
else:
    print()
    print('No!')
a = int(input())
b = int(input())
max_n_passes = int(input())
passes_cnt = 0
no_more_passwords = False

for symbol_1 in range(35, 56):
    for symbol_2 in range(64, 97):
        for num1 in range(1, a+1):
            for num2 in range(1, b+1):
                if symbol_1 > 55:
                    symbol_1 = 35
                if symbol_2 > 96:
                    symbol_2 = 64
                password = f'{chr(symbol_1)}{chr(symbol_2)}{num1}{num2}{chr(symbol_2)}{chr(symbol_1)}'
                print(password, end='|')
                passes_cnt += 1
                symbol_1 += 1
                symbol_2 += 1
                if passes_cnt >= max_n_passes or (a == num1 and b == num2):
                    no_more_passwords = True
                    break
            if no_more_passwords:
                break
        if no_more_passwords:
            break
    if no_more_passwords:
        break
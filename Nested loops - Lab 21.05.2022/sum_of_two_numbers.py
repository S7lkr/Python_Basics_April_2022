start_n = int(input())
end_n = int(input())
magic_n = int(input())
combinations_counter = 0
flag = False

for i in range(start_n, end_n + 1):
    for h in range(start_n, end_n + 1):
        combinations_counter += 1
        if i + h == magic_n:
            flag = True
            print(f'Combination N:{combinations_counter} ({i} + {h} = {magic_n})')
            break
    if flag:
        break

if not flag:
    print(f'{combinations_counter} combinations - neither equals {magic_n}')

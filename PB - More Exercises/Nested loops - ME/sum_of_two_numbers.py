start = int(input())
end = int(input())
magic_num = int(input())
counter = 0
combination_met = False

for i in range(start, end+1):
    for h in range(start, end+1):
        counter += 1
        if i + h == magic_num:
            print(f'Combination N:{counter} ({i} + {h} = {magic_num})')
            combination_met = True
            break
    if combination_met:
        break
else:
    print(f'{counter} combinations - neither equals {magic_num}')
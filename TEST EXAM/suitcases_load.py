trunk_capacity = float(input())

suitcase_cnt = 0
capacity_taken = 0
no_more_space = False

while True:
    suitcase = input()
    if suitcase == 'End':
        print('Congratulations! All suitcases are loaded!')
        print(f'Statistic: {suitcase_cnt} suitcases loaded.')
        break
    else:
        suitcase = float(suitcase)
        if capacity_taken + suitcase >= trunk_capacity:
            no_more_space = True
            break
        suitcase_cnt += 1
        if suitcase_cnt % 3 == 0:
            capacity_taken += suitcase + suitcase * 0.1
        else:
            capacity_taken += suitcase

if no_more_space:
    print('No more space!')
    print(f'Statistic: {suitcase_cnt} suitcases loaded.')
bottles_detergent = int(input())
detergent_total = 750 * bottles_detergent
detergent_left = detergent_total

dishes_cnt = 0
pots_cnt = 0
washes_cnt = 0
enough_detergent = False

while detergent_left >= 0:
    dishes_pots = input()
    if dishes_pots == 'End':
        enough_detergent = True
        break
    else:
        dishes_pots = int(dishes_pots)
        washes_cnt += 1
        if washes_cnt % 3 == 0:
            detergent_left -= dishes_pots * 15
            pots_cnt += dishes_pots
        else:
            detergent_left -= dishes_pots * 5
            dishes_cnt += dishes_pots

if enough_detergent:
    print('Detergent was enough!')
    print(f'{dishes_cnt} dishes and {pots_cnt} pots were washed.')
    print(f'Leftover detergent {detergent_left} ml.')
else:
    print(f'Not enough detergent, {abs(detergent_left)} ml. more necessary!')
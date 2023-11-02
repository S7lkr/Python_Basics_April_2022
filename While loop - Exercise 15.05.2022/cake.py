cake_length = int(input())
cake_width = int(input())

cake_area = cake_width * cake_length
total_pieces_taken = 0
no_more_cake = False

pieces_taken = input()
while pieces_taken != 'STOP':
    total_pieces_taken += int(pieces_taken)
    cake_area -= int(pieces_taken)
    if cake_area <= 0:
        break
    else:
        pieces_taken = input()

if cake_area < 1:
    no_more_cake = True

if no_more_cake:
    print(f'No more cake left! You need {abs(cake_area)} pieces more.')
else:
    print(f'{cake_area} pieces are left.')
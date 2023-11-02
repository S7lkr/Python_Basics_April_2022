last_sector = input()
first_sector_rows = int(input())
seats_n_odd_row = int(input())
seats_cnt = 0

for sector in range(65, ord(last_sector) + 1):
    if sector > 65:
        first_sector_rows += 1
    for row in range(1, first_sector_rows + 1):
        if row % 2 != 0:
            for seat in range(1, seats_n_odd_row + 1):
                    seat_number = f'{chr(sector)}{row}{chr(seat+96)}'
                    print(seat_number)
                    seats_cnt += 1
        else:
            for seat in range(1, (seats_n_odd_row+2) + 1):
                seat_number = f'{chr(sector)}{row}{chr(seat + 96)}'
                print(seat_number)
                seats_cnt += 1
print(seats_cnt)
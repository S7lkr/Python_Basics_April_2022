holiday_price = float(input())
n_puzzle = int(input())
n_doll = int(input())
n_teddy_bear = int(input())
n_minion = int(input())
n_truck = int(input())

n_toys = n_puzzle + n_doll + n_teddy_bear + n_minion + n_truck
earn = (n_puzzle * 2.60) + (n_doll * 3) + (n_teddy_bear * 4.10) + (n_minion * 8.20) + (n_truck * 2)

if n_toys >= 50:
    earn -= earn * 0.25

total_profit = earn - (earn * 0.10)
money_left = abs(total_profit - holiday_price)

if total_profit >= holiday_price:
    print(f'Yes! {money_left:.2f} lv left.')
else:
    print(f'Not enough money! {money_left:.2f} lv needed.')

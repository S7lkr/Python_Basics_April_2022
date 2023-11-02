fuel = input()
litres = float(input())
card = input()


gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
price = 0

if card == 'Yes':
    if fuel == 'Gasoline':
        gasoline_price -= 0.18
    elif fuel == 'Diesel':
        diesel_price -= 0.12
    elif fuel == 'Gas':
        gas_price -= 0.08
elif card == 'No':
    discount = 0

if fuel == 'Gas':
    price = litres * gas_price
elif fuel == 'Gasoline':
    price = litres * gasoline_price
elif fuel == 'Diesel':
    price = litres * diesel_price

if litres > 25:
    price -= price * 0.1
elif litres >= 20:
    price -= price * 0.08

print(f'{price:.2f} lv.')
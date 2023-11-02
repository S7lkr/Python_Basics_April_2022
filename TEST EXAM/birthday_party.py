rent = float(input())

cake_price = rent * 0.2
drinks_price = cake_price - (cake_price * 0.45)
animator_price = rent / 3

money_needed = rent + cake_price + drinks_price + animator_price

print(money_needed)
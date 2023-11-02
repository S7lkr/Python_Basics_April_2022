year_fee = int(input())     # year payment for a basketball training

snickers_price = year_fee - (year_fee * 0.40)
outfit_price = snickers_price - (snickers_price * 0.20)
basketball_price = outfit_price * 0.25
accessories = basketball_price * 0.20

overall = year_fee + snickers_price + outfit_price + basketball_price + accessories

print(overall)

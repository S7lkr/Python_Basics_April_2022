square_meters_tobe_greened = float(input())
price = square_meters_tobe_greened * 7.61
discount = price * 0.18
final_price = price - (price * 0.18)

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")

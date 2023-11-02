pen_packages = int(input())
marker_packages = int(input())
cleaning_agent_litres = int(input())
discount = int(input()) / 100

price = ((pen_packages * 5.80) + (marker_packages * 7.20) +
               (cleaning_agent_litres * 1.20))
final_price = price - (price * discount)

print(final_price)

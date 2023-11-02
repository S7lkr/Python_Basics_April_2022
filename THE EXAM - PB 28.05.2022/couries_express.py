package_kg = float(input())
service = input()
distance = int(input())

standard_price = 0
express_price = 0

if package_kg < 1:
    standard_price = distance * 0.03
elif 1 <= package_kg < 10:
    standard_price = distance * 0.05
elif 10 <= package_kg < 40:
    standard_price = distance * 0.1
elif 40 <= package_kg < 90:
    standard_price = distance * 0.15
elif 90 <= package_kg < 150:
    standard_price = distance * 0.2

if service == 'express':
    if package_kg < 1:
        express_price = distance * (package_kg * (0.8 * 0.03))
    elif 1 <= package_kg <= 9:
        express_price = distance * (package_kg * (0.4 * 0.05))
    elif 10 <= package_kg <= 39:
        express_price = distance * (package_kg * (0.05 * 0.1))
    elif 40 <= package_kg <= 89:
        express_price = distance * (package_kg * (0.02 * 0.15))
    elif 90 <= package_kg < 150:
        express_price = distance * (package_kg * (0.01 * 0.2))

    express_price += standard_price

if service == 'standard':
    print(f'The delivery of your shipment with weight of {package_kg:.3f} kg. would cost {standard_price:.2f} lv.')
else:
    print(f'The delivery of your shipment with weight of {package_kg:.3f} kg. would cost {express_price:.2f} lv.')
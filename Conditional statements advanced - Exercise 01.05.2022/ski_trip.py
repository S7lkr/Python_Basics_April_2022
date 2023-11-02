# Total overnights in hotel
days_to_stay = int(input())
room_type = input()
mark = input()

nights_to_stay = days_to_stay - 1
price = 0
total_price = 0
discount = 0
mark_discount = 0

if room_type == 'room for one person':
    price = nights_to_stay * 18
elif room_type == 'apartment':
    price = nights_to_stay * 25
    if days_to_stay < 10:
        discount = 0.3
    elif 10 <= days_to_stay <= 15:
        discount = 0.35
    else:
        discount = 0.5
elif room_type == 'president apartment':
    price = 35 * nights_to_stay
    if days_to_stay < 10:
        discount = 0.1
    elif 10 <= days_to_stay <= 15:
        discount = 0.15
    else:
        discount = 0.2

if mark == 'positive':
    mark_discount = -0.25
elif mark == 'negative':
    mark_discount = 0.1


price -= price * discount
total_price = price - (price * mark_discount)

print(f'{total_price:.2f}')

t_shirt_price = float(input())
needed_sum = float(input())
card = input()

shorts_price = t_shirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = (t_shirt_price + shorts_price) * 2

total_sum = shorts_price + socks_price + shoes_price + t_shirt_price
if card == 'VIP':
    total_sum -= total_sum * 0.15
elif card == 'credit':
    total_sum = total_sum - (total_sum - 0.4)

if needed_sum <= total_sum:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_sum:.2f} lv.')
else:
    print('No, he will not earn the world-cup replica ball.')
    diff = abs(needed_sum - total_sum)
    print(f'He needs {diff:.2f} lv. more.')
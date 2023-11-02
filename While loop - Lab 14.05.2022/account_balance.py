balance = 0

while True:
    amount = input()
    if amount == 'NoMoreMoney':
        break
    amount = float(amount)

    if amount < 0:
        print('Invalid operation!')
        break
    balance += amount
    print(f'Increase: {amount:.2f}')

print(f'Total: {balance:.2f}')
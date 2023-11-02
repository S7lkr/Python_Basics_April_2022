project = input()
r = int(input())
c = int(input())

income = 0

if project == 'Premiere':
    income = (r * c) * 12
elif project == "Normal":
    income = (r * c) * 7.50
elif project == "Discount":
    income = (r * c) * 5

print(f'{income:.2f} leva')
tabs = int(input())
salary = int(input())

penalty = 0
total_penalty = 0

for num in range(tabs):
    website = input()
    if website == 'Facebook':
        penalty = 150
        total_penalty += 150
    elif website == 'Instagram':
        penalty = 100
        total_penalty += 100
    elif website == 'Reddit':
        penalty = 50
        total_penalty += 50

    if total_penalty >= salary:
        print('You have lost your salary.')
        break
    else:
        continue

if salary > total_penalty:
    diff = salary - total_penalty
    print(f'{diff}')
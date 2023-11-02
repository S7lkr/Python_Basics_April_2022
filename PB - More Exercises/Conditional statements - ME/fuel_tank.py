fuel = input()
litres = int(input())

if fuel != 'Diesel' and fuel != 'Gasoline' and fuel != 'Gas':
    print('Invalid fuel!')
elif litres >= 25:
    if fuel == 'Diesel':
        print('You have enough diesel.')
    elif fuel == 'Gasoline':
        print('You have enough gasoline.')
    else:
        print('You have enough gas.')
else:
    if fuel == 'Diesel':
        print(f'Fill your tank with diesel!')
    elif fuel == 'Gasoline':
        print(f'Fill your tank with gasoline!')
    else:
        print(f'Fill your tank with gas!')

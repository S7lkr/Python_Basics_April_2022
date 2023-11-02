from math import ceil
from math import floor

x = int(input())
y = float(input())
z = int(input())
workers = int(input())

kg_grape = (0.4 * x) * y
litres_wine = kg_grape / 2.5
diff = abs(litres_wine - z)
wine_for_1_worker = diff / workers

if litres_wine >= z:
    print(f'Good harvest this year! Total wine: {floor(litres_wine)} liters.')
    print(f'{ceil(diff)} liters left -> {ceil(wine_for_1_worker)} liters per person.')
else:
    print(f'It will be a tough winter! More {floor(diff)} liters wine needed.')
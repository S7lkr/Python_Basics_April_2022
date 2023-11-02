veg_1_kg = float(input())
fr_1_kg = float(input())
total_veg_kg = int(input())
total_fr_kg = int(input())

vegetables = total_veg_kg * veg_1_kg
fruits = total_fr_kg * fr_1_kg
total_profit = vegetables + fruits

print(f'{total_profit / 1.94:.2f}')
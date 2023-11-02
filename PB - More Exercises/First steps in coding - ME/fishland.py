mackerel_kg = float(input())
sprat_kg = float(input())
bonito_kg = float(input())
scad_kg = float(input())
mussels_kg = int(input())

bonito_price = bonito_kg * (mackerel_kg * 1.6)
scad_price = scad_kg * (sprat_kg * 1.8)
mussels_price = mussels_kg * 7.5
total = bonito_price + scad_price + mussels_price

print(f'{total:.2f}')
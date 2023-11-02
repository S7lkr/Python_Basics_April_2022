nylon_sq_meter = int(input())   # square meters of nylon needed
paint = int(input())    # litres of paint
acetone = int(input())   # litres of acetone
hours_to_finish_the_work = int(input())     # hours needed for the workers to finish the job

nylon_price = (nylon_sq_meter + 2) * 1.5
paint_price = (paint * 14.50)
paint_price += (paint * 14.50) * 0.10
acetone_price = acetone * 5.0

total_price_materials = nylon_price + paint_price + acetone_price + 0.40
payment_for_workers = (0.30 * total_price_materials) * hours_to_finish_the_work
overall = total_price_materials + payment_for_workers

print(f'{overall}')

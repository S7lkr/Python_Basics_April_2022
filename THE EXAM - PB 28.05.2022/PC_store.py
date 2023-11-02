cpu_price = float(input())
gpu_price = float(input())
ram_price = float(input())
ram_amount = int(input())
discount = float(input())

cpu_price *= 1.57
gpu_price *= 1.57
ram_price *= 1.57
ram_price *= ram_amount

cpu_price -= cpu_price * discount     # cpu_price = cpu_price -(cpu_price * discount)
gpu_price -= gpu_price * discount

money_needed = cpu_price + gpu_price + ram_price

print(f'Money needed - {money_needed:.2f} leva.')
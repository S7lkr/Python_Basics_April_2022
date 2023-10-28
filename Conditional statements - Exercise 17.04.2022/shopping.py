budget = float(input())
n_gpu = int(input())
n_cpu = int(input())
n_ram = int(input())

gpu_price = n_gpu * 250
cpu_price = n_cpu * (0.35 * gpu_price)
ram_price = n_ram * (0.10 * gpu_price)

total_price = gpu_price + cpu_price + ram_price

if n_gpu > n_cpu:
    discount = total_price * 0.15
    total_price -= discount

difference = abs(budget - total_price)

if budget >= total_price:
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')
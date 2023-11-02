n = int(input())

p1 = 0  # Amount of numbers lesser than 200
p2 = 0  # From 200 to 399
p3 = 0  # From 400 to 599
p4 = 0  # from 600 to 799
p5 = 0  # above 800

for num in range(1, n + 1):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    if 200 <= current_num <= 399:
        p2 += 1
    if 400 <= current_num <= 599:
        p3 += 1
    if 600 <= current_num <= 799:
        p4 += 1
    if current_num >= 800:
        p5 += 1

# We transform the different amount of numbers into percents, using this formula:
# i.e. p1 = {amount of numbers < 200} from total 20 numbers (loops) multiplied by 100
p1 = (p1 / n) * 100
p2 = (p2 / n) * 100
p3 = (p3 / n) * 100
p4 = (p4 / n) * 100
p5 = (p5 / n) * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
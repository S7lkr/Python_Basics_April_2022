pool_capacity = int(input())
p1 = int(input())
p2 = int(input())
hours_away = float(input())

p1_l = p1 * hours_away
p2_l = p2 * hours_away

if pool_capacity >= (p1_l + p2_l):
    pool_fullness = ((p1_l + p2_l) / pool_capacity) * 100
    p1_filled = p1_l / (p1_l + p2_l) * 100
    p2_filled = p2_l / (p1_l + p2_l) * 100
    print(f'The pool is {pool_fullness:.2f}% full. Pipe 1: {p1_filled:.2f}%. Pipe 2: {p2_filled:.2f}%.')
else:
    overflow = (p1_l + p2_l) - pool_capacity
    print(f'For {hours_away} hours the pool overflows with {overflow:.2f} liters.')
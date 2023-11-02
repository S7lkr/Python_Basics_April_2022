total_steps = 0
time_to_go = False

while total_steps < 10000:
    steps = input()
    if time_to_go:
        total_steps += int(steps)
        break
    if steps != 'Going home':
        total_steps += int(steps)
    else:
        time_to_go = True
        continue

diff = abs(total_steps - 10000)

if total_steps >= 10000:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')

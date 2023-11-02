name = input()
points = float(input())
judge_count = int(input())

total_judge_points = 0

for _ in range(judge_count):
    judge_name = input()
    judge_points = float(input())

    total_judge_points = ((len(judge_name) * judge_points) / 2)
    points += total_judge_points

    if points >= 1250.5:
        print(f'Congratulations, {name} got a nominee for leading role with {points:.1f}!')
        break

if points < 1250.5:
    diff = 1250.5 - points
    print(f'Sorry, {name} you need {diff:.1f} more!')
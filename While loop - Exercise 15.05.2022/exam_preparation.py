n_poor_grades = int(input())

task_count = 0
last_task = ''
sum_grades = 0
poor_grades_count = 0

while True:
    task = input()
    if task == 'Enough':
        break

    grade = int(input())
    if grade <= 4:
        poor_grades_count += 1
    if poor_grades_count >= n_poor_grades:
        print(f'You need a break, {n_poor_grades} poor grades.')
        break
    task_count += 1
    sum_grades += grade
    last_task = task

if poor_grades_count < n_poor_grades:
    average_score = sum_grades / task_count
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {task_count}')
    print(f'Last problem: {last_task}')
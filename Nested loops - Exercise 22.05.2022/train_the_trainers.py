n_judges = int(input())

sum_of_marks = 0
sum_of_average_marks = 0
presentations_cnt = 0
marks_cnt = 0

have_finished = False

presentation = input()
while marks_cnt <= n_judges:
    if presentation == 'Finish':
        have_finished = True
        break
    presentations_cnt += 1
    for j in range(1, n_judges + 1):
        mark = float(input())
        sum_of_marks += mark
        marks_cnt += 1

    average_mark = sum_of_marks / n_judges
    sum_of_average_marks += average_mark
    print(f'{presentation} - {average_mark:.2f}.')
    sum_of_marks = 0
    marks_cnt = 0
    presentation = input()

if have_finished:
    print(f'Student\'s final assessment is {sum_of_average_marks / presentations_cnt:.2f}.')
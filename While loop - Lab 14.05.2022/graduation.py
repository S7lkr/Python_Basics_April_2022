name = input()

total_sum_marks = 0
class_n = 0
failure = 0

while failure <= 1:
    grade = float(input())
    if grade >= 4:
        total_sum_marks += grade
        class_n += 1
    else:
        failure += 1
    if class_n == 12:
        average_mark = total_sum_marks / 12
        print(f'{name} graduated. Average grade: {average_mark:.2f}')
        break
else: 
    print(f'{name} has been excluded at {class_n + 1} grade')
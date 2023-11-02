group_count = int(input())

total_people = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for _ in range(group_count):
    people_in_group = int(input())
    total_people += people_in_group
    if people_in_group <= 5:
        p1 += people_in_group
    elif 6 <= people_in_group <= 12:
        p2 += people_in_group
    elif 13 <= people_in_group <= 25:
        p3 += people_in_group
    elif 26 <= people_in_group <= 40:
        p4 += people_in_group
    elif people_in_group >= 41:
        p5 += people_in_group

p1 = (p1 / total_people) * 100
p2 = (p2 / total_people) * 100
p3 = (p3 / total_people) * 100
p4 = (p4 / total_people) * 100
p5 = (p5 / total_people) * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
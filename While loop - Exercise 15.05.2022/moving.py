width = int(input())
length = int(input())
height = int(input())

space_available = width * length * height
no_more_space = False

while space_available > 0:
    n_boxes = input()
    if n_boxes == 'Done':
        no_more_space = True
        break
    else:
        space_available -= int(n_boxes)

if no_more_space:
    print(f'{space_available} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(space_available)} Cubic meters more.')
number = int(input())
pyramid_is_ready = False
counter = 1
for rows in range(1, number + 1):
    for col in range(rows):
        if counter > number:
            pyramid_is_ready = True
            break
        print(counter, end=' ')
        counter += 1
    print()
    if pyramid_is_ready:
        break
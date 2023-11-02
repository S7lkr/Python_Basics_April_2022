n1 = int(input())
n2 = int(input())

operator = input()
result = 0
even_odd = ''

if operator == '+':
    operator = '+'
    result = n1 + n2
elif operator == '-':
    operator = '-'
    result = n1 - n2
elif operator == '*':
    operator = '*'
    result = n1 * n2
elif operator == '/':
    operator = '/'
    if n2 != 0:
        result = n1 / n2
        print(f'{n1} / {n2} = {result:.2f}')
    else:
        print(f'Cannot divide {n1} by zero')
elif operator == '%':
    operator = '%'
    if n2 != 0:
        result = n1 % n2
        print(f'{n1} % {n2} = {result}')
    else:
        print(f'Cannot divide {n1} by zero')

if operator == '+' or operator == '-' or operator == '*':
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {even_odd}')

# if n2 != 0:
#     if operator == '/':
#         print(f'{n1} / {n2} = {result:.2f}')
#     elif operator == '%':
#         print(f'{n1} % {n2} = {result}')
# else:
#     print(f'Cannot divide {n1} by zero')
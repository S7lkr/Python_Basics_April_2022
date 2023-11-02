# We want the input number as a string. Why? Because we will start the 'while loop'  with comparing it
# with another string, called 'stop'
number = input()

# We are going to add every single prime number here
prime_sum = 0
# Also, for the non-prime numbers. They will stack here
non_prime_sum = 0

# First we make this check. If it is False, the loop will not engage and the program will end
while number != 'stop':
    # Then immediately we convert the type of 'number' into 'int', because we need it as a number from now on
    number = int(number)
    # First we take care of special (edge) cases
    if number < 0:
        print('Number is negative.')
        number = input()
        continue
    elif number == 0:
        non_prime_sum += number
        number = input()
        continue
    elif number == 1:
        prime_sum += number
        number = input()
        continue
    else:
        # When we enter this 'else' we are sure the 'number' is neither Negative, nor 0, nor 1
        # We want to set a flag 'is_prime = True'
        # Which means: IT'S TRUE that the number is PRIME (for now)
        is_prime = True
    for div in range(2, number):
        if number % div == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum += number
    else:
        non_prime_sum += number

    number = input()
print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')
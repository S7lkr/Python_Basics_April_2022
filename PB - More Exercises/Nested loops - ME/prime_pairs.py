num1 = int(input())
num2 = int(input())
add1 = int(input())
add2 = int(input())

end1 = num1 + add1
end2 = num2 + add2


for a in range(num1, end1 + 1):
    for b in range(num2, end2+1):
        for div in range(2, a):
            if a % div == 0:
                break
        else:
            for div2 in range(2, b):
                if b % div2 == 0:
                    break
            else:
                two_primes = f'{a}{b}'
                print(two_primes)
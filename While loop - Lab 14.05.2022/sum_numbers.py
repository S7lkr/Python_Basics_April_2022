# result = int(input())
# suma = 0
#
# while suma < result:
#     number = int(input())
#     suma += number
# print(suma)

result = int(input())
suma = 0

while True:
    number = int(input())
    suma += number
    if suma >= result:
        print(suma)
        break
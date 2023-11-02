# user = input()
# password = input()
#
# user_pass = input()
#
# while password != user_pass:
#     user_pass = input()
# print(f'Welcome {user}!')

user = input()
password = input()

while True:
    user_pass = input()
    if user_pass == password:
        break
print(f'Welcome {user}!')
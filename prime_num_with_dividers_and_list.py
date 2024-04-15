# Prime Numbers - divides ONLY by 1 and itself -> 2, 3, 5, 7, 11, 13, 17, 19 ...
# Not-Prime Numbers - divides by 1, itself and at least one more divider -> 4, 6, 8, 9, 10, 12, 14, 15 ...

# Prime/Non-prime NUMBER with Number of dividers & Dividers list:
def prime_msg(num: int) -> str:
    return f'{num} is a PRIME number!'


def not_prime_msg(num: int, divs: list or str = '') -> str:
    return (f'"{num}" is NOT a PRIME number! It has {exceptional_num[num] if num < 3 else len(dividers_list)} divider/s'
            f'{". " + _except if num in (0, 1, 2) else ": " + str(divs)}')


def check_if_number_0_1_2(num: int) -> bool:                # if num = 0, 1 or 2 execute line 9
    return 0 <= num < 3                                    # IF number IN (0, 1, 2) !!


def prime_validator(number: int) -> str:                    # this func. calls another func (line 24)
    if prime_number_checker(number):
        return not_prime_msg(number, dividers_list)
    return prime_msg(number)                                # --> line 5


def prime_number_checker(num: int) -> bool:                 # this is the "bottom" function. It doesn't call any func
    div_cnt: int = 0                                        # It judges if "num" is PRIME or NOT
    for div in range(2, num//2 + 1):
        if num % div == 0:
            div_cnt += 1
            dividers_list.append(div)
    return div_cnt > 0                                      # returns TRUE/FALSE


def main_logic(num: int) -> str:                      # START main_function
    if check_if_number_0_1_2(num):                    # first check --> line 14. If true:
        return not_prime_msg(num)                     # <-- print number is exceptional!
    return prime_validator(num)                       # --> else engage another check --> line 18


# START
# INPUT & Validation Section:
try:                            # проверява дали n.__class__.__name__ == "int"
    n = int(input("Enter a valid POSITIVE INTEGER number: "))           # вход
except ValueError as err:       # ако НЕ, то хвани ValueError грешка със съобщение:
    print(f"Input is invalid! Please be GOOD and enter a VALID data type! Thank you! :)")
else:
    if n < 0:
        raise Exception(f'''Number "{n}" must be a POSITIVE INTEGER value! Please convert '''
                        f'''"{n}" to "{abs(n)}" (if you don't know how, ask YOUR TEACHER) and try again! :)''')

    # variables used by the code:
    _except: str = "It is an exception!!"
    dividers_list: list = list()
    exceptional_num: dict = {
        0: "unlimited".upper(),
        1: "NO",
        2: "NO"
    }

    # Proceed to executing the main func:
    print(main_logic(n))

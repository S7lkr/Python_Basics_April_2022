money_in_coins = int(float(input()) * 100)
coins = 0

one_st = 0
two_st = 0
five_st = 0
ten_st = 0
twenty_st = 0
fifty_st = 0
one_lev = 0
two_leva = 0

while money_in_coins >= 1:
    if money_in_coins // 200 >= 1:
       two_leva = money_in_coins // 200
       coins += two_leva
       money_in_coins -= two_leva * 200
    elif money_in_coins // 100 >= 1:
        one_lev = money_in_coins // 100
        coins += one_lev
        money_in_coins -= one_lev * 100
    elif money_in_coins // 50 >= 1:
        fifty_st = money_in_coins // 50
        coins += fifty_st
        money_in_coins -= fifty_st * 50
    elif money_in_coins // 20 >= 1:
        twenty_st = money_in_coins // 20
        coins += twenty_st
        money_in_coins -= twenty_st * 20
    elif money_in_coins // 10 >= 1:
        ten_st = money_in_coins // 10
        coins += ten_st
        money_in_coins -= ten_st * 10
    elif money_in_coins // 5 >= 1:
        five_st = money_in_coins // 5
        coins += five_st
        money_in_coins -= five_st * 5
    elif money_in_coins // 2 >= 1:
        two_st = money_in_coins // 2
        coins += two_st
        money_in_coins -= two_st * 2
    elif money_in_coins // 1 == 1:
        one_st = money_in_coins // 1
        coins += one_st
        money_in_coins -= one_st * 1
        break
print(round(coins))
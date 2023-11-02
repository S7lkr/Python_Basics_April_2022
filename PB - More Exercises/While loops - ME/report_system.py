donation_expected = int(input())

sum_gathered = 0
transaction_cnt = 0

people_credit_card = 0
credit_card_sum = 0
people_cash = 0
cash_sum = 0
donation_gathered = False

while sum_gathered < donation_expected:
    product_price = input()
    if product_price == 'End':
        print('Failed to collect required money for charity.')
        break
    else:
        product_price = int(product_price)
        transaction_cnt += 1
        if 10 <= product_price <= 100:
            sum_gathered += product_price
            print('Product sold!')
            # плащане с пари в брой щото е първи път, т.е. нечетен
            if transaction_cnt % 2 != 0:
                people_cash += 1
                cash_sum += product_price
            else:
                people_credit_card += 1
                credit_card_sum += product_price
        elif product_price <= 9:
            if transaction_cnt % 2 != 0:
                print('Product sold!')
                sum_gathered += product_price
                people_cash += 1
            else:
                print('Error in transaction!')
        else:   # if product_price > 100:
            # Плащане с карта, щото е четен път плащане
            if transaction_cnt % 2 == 0:
                print('Product sold!')
                sum_gathered += product_price
                credit_card_sum += product_price
                people_credit_card += 1
            else:
                print('Error in transaction!')
else:
    donation_gathered = True

if donation_gathered:
    average_cash = cash_sum / people_cash
    average_credit = credit_card_sum / people_credit_card
    print(f'Average CS: {average_cash:.2f}')
    print(f'Average CC: {average_credit:.2f}')
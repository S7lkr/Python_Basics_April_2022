letter = ''
con_letters = ''
word = ''
secret_word = ''

while letter != 'End':
    letter = input()
    if letter.isalpha():
        if letter == 'c':
            if 'c' in con_letters:
                word += 'c'
            con_letters += 'c'
        elif letter == 'o':
            if 'o' in con_letters:
                word += 'o'
            con_letters += 'o'
        elif letter == 'n':
            if 'n' in con_letters:
                word += 'n'
            con_letters += 'n'
        else:
            word += letter
        if ('c' in con_letters) and ('o' in con_letters) and ('n' in con_letters):
            word += ' '
            secret_word += word
            word = ''
            con_letters = ''
            continue

print(secret_word)
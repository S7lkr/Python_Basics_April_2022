# book = input()
# lib_book = input()
# checked_books = 0
#
# while lib_book != 'No More Books':
#     if lib_book != book:
#         checked_books += 1
#         lib_book = input()
#     else:
#         print(f'You checked {checked_books} books and found it.')
#         break
# else:
#     print('The book you search is not here!')
#     print(f'You checked {checked_books} books.')

fav_book = input()
book_found = False
books_checked = 0

curr_book = input()
while curr_book != 'No More Books':
    if curr_book == fav_book:
        book_found = True
        break
    else:
        books_checked += 1
        curr_book = input()
if book_found:
    print(f'You checked {books_checked} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {books_checked} books.')
all_pages = int(input())
pages_read_for_1_hour = int(input())
days_to_finish_book = int(input())

reading_book_hours = all_pages / pages_read_for_1_hour
hours_per_day = reading_book_hours // days_to_finish_book

print(hours_per_day)
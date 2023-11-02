money = int(input())
months = int(input())
year_increase_percent = float(input()) * 0.01

gained_sum = ((money * year_increase_percent)/12) * months + money

print(gained_sum)
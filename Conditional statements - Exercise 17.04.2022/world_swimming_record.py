world_record = float(input())
# Total distance for swimming
distance = float(input())
# Seconds needed to swim 1 meter in water
seconds_for_1_meter = float(input())

# The seconds added to Ivan's time, because of the water resistance. Every 15 meters we add 12.5 seconds more
# NOTE: We use INTEGER DIVISION for meters!!
water_resistance = (distance // 15) * 12.5
# Total amount of time (seconds) needed to complete the distance
ivan_record = seconds_for_1_meter * distance + water_resistance

if ivan_record < world_record:
    print(f'Yes, he succeeded! The new world record is {ivan_record:.2f} seconds.')
else:
    time_needed = ivan_record - world_record
    print(f'No, he failed! He was {time_needed:.2f} seconds slower.')

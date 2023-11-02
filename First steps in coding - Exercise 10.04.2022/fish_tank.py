length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

# all the cube centimeters, needed to fill the aquarium, BUT converted into cubic meters
litres_needed = (length * width * height) * 0.001
litres_needed -= (litres_needed * percent)

print(litres_needed)

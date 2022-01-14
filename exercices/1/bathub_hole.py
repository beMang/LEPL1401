import math

filled_time = 80.0/11.0

minute = 0

water_vol = 0
for minute in range(math.ceil(filled_time)):
    water_vol = water_vol + 12 - 1

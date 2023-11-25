# program to convert kilometers & meters
# convert7.38 miles to kilometers
# convert 72.25 kilometers to miles
# 1m = 1.61km
# round() function rounds the decimal places to the specified number

kilometers = 72.25

miles = 7.38

miles_to_kilometers = miles * (1.61/1)

kilometers_to_miles = (kilometers) / 1.61

print(miles, 'miles is equal to', round(miles_to_kilometers, 2), 'kilometers')

print(kilometers, 'kilometers is equal to', round(kilometers_to_miles, 2), 'miles')

# Python Math Module Practice

import math

numbers = [4, 9, 16, 25]

for number in numbers:
    print("Square root of", number, ":", math.sqrt(number))

print("Power:", math.pow(2, 5))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))
print("Absolute value:", abs(-25))

print("GCD:", math.gcd(24, 36))

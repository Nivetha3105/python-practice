# Check whether a number is even or odd

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


number = 17

result = check_even_odd(number)

print(number, "is", result)

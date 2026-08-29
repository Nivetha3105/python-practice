# Find the factorial of a number

def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers"

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


number = 5

print("Factorial of", number, "is", factorial(number))

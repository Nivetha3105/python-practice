

try:
    number = int("25")
    result = 100 / number
    print("Result:", result)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program execution completed")



try:
    age = int("twenty")
    print("Age:", age)

except ValueError:
    print("Please enter a valid number")

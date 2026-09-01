# Reverse a number

def reverse_number(number):
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return reversed_number


number = 12345

print("Original number:", number)
print("Reversed number:", reverse_number(number))

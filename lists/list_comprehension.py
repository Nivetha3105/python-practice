# Python List Comprehension Practice

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squares
squares = [x * x for x in numbers]
print("Squares:", squares)

# Even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# Odd numbers
odd_numbers = [x for x in numbers if x % 2 != 0]
print("Odd numbers:", odd_numbers)

# Numbers greater than 5
greater_than_five = [x for x in numbers if x > 5]
print("Greater than 5:", greater_than_five)

# Convert words to uppercase
words = ["python", "react", "fastapi"]
uppercase_words = [word.upper() for word in words]
print("Uppercase:", uppercase_words)

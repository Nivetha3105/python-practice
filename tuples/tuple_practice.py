# Python Tuple Practice

numbers = (10, 20, 30, 40, 50)

# 1. Access elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# 2. Find length
print("Length:", len(numbers))

# 3. Count an element
print("Count of 20:", numbers.count(20))

# 4. Find the position of an element
print("Position of 30:", numbers.index(30))

# 5. Check if an element exists
print("Is 40 present?", 40 in numbers)

# 6. Slice a tuple
print("First three elements:", numbers[:3])

# 7. Tuple unpacking
a, b, c, d, e = numbers
print("Unpacked values:", a, b, c, d, e)

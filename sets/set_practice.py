# Python Set Practice

numbers = {10, 20, 30, 20, 40, 10}

# Duplicate values are automatically removed
print("Set:", numbers)

# 1. Add an element
numbers.add(50)
print("After adding 50:", numbers)

# 2. Remove an element
numbers.remove(20)
print("After removing 20:", numbers)

# 3. Check if an element exists
print("Is 30 present?", 30 in numbers)

# 4. Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

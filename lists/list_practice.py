

numbers = [10, 20, 30, 40, 50]


print("First element:", numbers[0])

numbers.append(60)
print("After append:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)


numbers.remove(30)
print("After remove:", numbers)


print("Largest:", max(numbers))
print("Smallest:", min(numbers))


print("Sum:", sum(numbers))


numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

# Python Counter Practice

from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

frequency = Counter(numbers)

print("Frequency:", frequency)
print("Count of 3:", frequency[3])
print("Most common:", frequency.most_common(2))

text = "programming"

letter_count = Counter(text)

print("Letter frequency:", letter_count)

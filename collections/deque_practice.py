# Python Deque Practice

from collections import deque

queue = deque()

queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")

print("Queue:", queue)

first_person = queue.popleft()
print("Removed:", first_person)
print("Queue after removal:", queue)

queue.appendleft("David")
print("After adding to front:", queue)

last_person = queue.pop()
print("Removed from end:", last_person)
print("Final queue:", queue)

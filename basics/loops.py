
for i in range(1, 11):
    print(i)


print("Even numbers:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


total = 0
for i in range(1, 11):
    total += i

print("Sum:", total)


count = 1
while count <= 5:
    print("Count:", count)
    count += 1

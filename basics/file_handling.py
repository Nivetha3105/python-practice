# Python File Handling Practice

file_name = "sample.txt"

with open(file_name, "w") as file:
    file.write("Python file handling practice\n")
    file.write("Learning Python step by step.")


with open(file_name, "r") as file:
    content = file.read()

print("File content:")
print(content)

with open(file_name, "a") as file:
    file.write("\nPracticing every day.")

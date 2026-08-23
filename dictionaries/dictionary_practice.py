

student = {
    "name": "Nivetha",
    "age": 19,
    "course": "Computer Science",
    "gpa": 8.3
}

print("Name:", student["name"])
print("Course:", student["course"])

student["city"] = "Chennai"
print("After adding city:", student)


student["gpa"] = 8.5
print("Updated GPA:", student["gpa"])


print("Is age present?", "age" in student)

print("Keys:", student.keys())

print("Values:", student.values())

for key, value in student.items():
    print(key, ":", value)


student.pop("age")
print("After removing age:", student)



text = "Python Programming"


print("Length:", len(text))

print("Uppercase:", text.upper())


print("Lowercase:", text.lower())


print("Reversed:", text[::-1])


word = "Python"
print("Contains Python:", word in text)


print("Count of 'm':", text.count("m"))


new_text = text.replace("Python", "Java")
print("After replacement:", new_text)

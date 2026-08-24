

text = "  Python Programming  "


clean_text = text.strip()
print("Stripped:", clean_text)

print("Uppercase:", clean_text.upper())
print("Lowercase:", clean_text.lower())
print("Title case:", clean_text.title())

print("Starts with Python:", clean_text.startswith("Python"))
print("Ends with Programming:", clean_text.endswith("Programming"))


print("Position of Programming:", clean_text.find("Programming"))


updated_text = clean_text.replace("Programming", "Development")
print("Updated:", updated_text)


words = clean_text.split()
print("Words:", words)


joined = "-".join(words)
print("Joined:", joined)
